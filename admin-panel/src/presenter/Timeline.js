import TimelineView from "../view/TimelineView.js"

import "react-calendar-timeline/lib/Timeline.css"
import moment from "moment"

import {useList} from "react-firebase-hooks/database"
import {push, ref, set} from "firebase/database"
import {db} from "../api/firebase.js"

import {useNavigate, useParams} from "react-router-dom"
import {getHours, getMinutes, setHours, setMinutes} from "date-fns";
import {useState} from "react";

export default function TimelinePresenter() {
    const {boxId} = useParams()
    const navigate = useNavigate()

    const [bookings, loadingBookings, errorBookings] = useList(ref(db, `keyboxes/${boxId}/bookings`))
    const [keys, loadingKeys, errorKeys] = useList(ref(db, `keyboxes/${boxId}/keys`))

    const [selectedBooking, setSelectedBooking] = useState({});


    if (errorBookings || errorKeys) return <div>Something went wrong</div>

    const groups = keys
        .map(key => ({...key.val(), id: key.key}))
        .map(({name, id}) => ({
            id,
            title: name,
        }))

    const items = bookings
        .map(b => ({...b.val(), id: b.key}))
        .map(b => ({
            ...b, group: b.keyId, title: b.name,
            start_time: moment(b.checkIn * 1000),
            end_time: moment(b.checkOut * 1000),
            itemProps: {
                // these optional attributes are passed to the root <div /> of each item as <div {...itemProps} />
                'data-custom-attribute': 'Random content',
                'aria-hidden': true,
                onDoubleClick: () => {
                    console.log('You clicked double!')
                },
                className: 'weekend',
                style:
                    moment(b.checkOut * 1000) < moment() ?
                        {
                            background: '#ff0073',
                            backgroundColor: '#ff0073',
                            border: '#ff0073',
                            'color': 'white',
                            'font-family': 'Source Sans Pro, sans-serif',
                            'font-size': 14,
                            'overflow': 'clip',
                            'border-radius': '8px',
                        }
                        : {
                            background: '#04AA6D',
                            backgroundColor: '#04AA6D',
                            border: '#04AA6D',
                            'color': 'white',
                            'font-family': 'Source Sans Pro, sans-serif',
                            'font-size': 14,
                            'overflow': 'clip',
                            'border-radius': '8px',
                        },

            }
        }))
    /*
     const populatedBookings = bookings
         .map(b => ({ ...b.val(), id: b.key}))
         .map(b => ({ ...b, room: keyInfo[b.keyId]?.name, checkIn: FormatDate(b.checkIn), checkOut: FormatDate(b.checkOut)}))
     */
    const handleBookingMove = (bookingId, newStartTime, key) => {
        let confirmAction = window.confirm("Please confirm you want to change the date of this booking.");
        if (!confirmAction) {
            return;
        }

        const booking = items.find(booking => booking.id === bookingId);

        const checkIn = new moment(newStartTime).set({
            hour: booking.start_time.hour(),
            minute: booking.start_time.minute()
        }).unix();

        const checkOut = new moment(checkIn * 1000).add(booking.end_time.diff(booking.start_time, 'minute'), "minute").set({
            hour: booking.end_time.hour(),
            minute: booking.end_time.minute()
        }).unix();

        const updatedBooking = {
            checkIn: checkIn,
            checkOut: checkOut,
            email: booking.email,
            keyId: key.id,
            message: booking.message,
            name: booking.title,
        };
        console.log(booking);
        console.log(updatedBooking);
        console.log({
            1: new Date(booking.checkIn * 1000).toString(),
            2: new Date(booking.checkOut * 1000).toString(),
            3: new Date(updatedBooking.checkIn * 1000).toString(),
            4: new Date(updatedBooking.checkOut * 1000).toString(),
        });


        set(ref(db, "keyboxes/" + boxId + "/bookings/" + bookingId), updatedBooking)
            .then(() => {
            })
            .catch(error => alert("Something went wrong " + error.message))

    }

    const handleBookingDelete = () => {
        let confirmAction = window.confirm("Please confirm you want to delete the booking.");
        if (confirmAction) {
            set(ref(db, "keyboxes/" + boxId + "/bookings/" + selectedBooking.id), {})
                .then(() => {
                })
                .catch(error => alert("Something went wrong " + error.message))
            //handleDeSelectingBooking();
        } else {
            alert("Canceled");
        }
    }
    const handleDeSelectingBooking = () => {
        setSelectedBooking({});
    }
    const handleSelectingBooking = (itemId) => {
        let sel = items.find(booking => booking.id === itemId);
        console.log(sel)
        setSelectedBooking({
            ...sel,
            start_time: sel.start_time.format("hh:mm"),
            end_time: sel.end_time.format("hh:mm"),
        });
    }

    const handleNewBooking = (keyId, time) => {
        const startDate = time;

        console.log({keyId, startDate})
        navigate(`/${boxId}/new-booking`);
    }

    console.log(items)

    return <TimelineView groups={groups}
                         items={items}
                         loading={loadingBookings || loadingKeys}
                         selectedBooking={selectedBooking}

                         handleBookingMove={handleBookingMove}
                         handleSelectingBooking={handleSelectingBooking}
                         handleNewBooking={handleNewBooking}
                         handleBookingDelete={handleBookingDelete}
                         handleDeSelectingBooking={handleDeSelectingBooking}/>
}
