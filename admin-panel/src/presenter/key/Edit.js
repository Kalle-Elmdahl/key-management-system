import { onValue, ref, set } from "firebase/database"
import { useState, useEffect } from "react"
import { useNavigate, useParams } from "react-router-dom"
import { db } from "../../api/firebase"
import EditKeyView from "../../view/key/EditView"
import KeyFormView from "../../view/key/FormView"

import useRelativeNavigation from "../../hooks/useRelativeNavigation"
import useTitle from "../../hooks/useTitle"
import { format } from "date-fns"

let lastReadData = {}

export default function EditKeyPresenter() {
    useTitle("Edit key")
	const { boxId, keyId } = useParams()
	const navigate = useNavigate()
	const relativeNavigate = useRelativeNavigation()
	const [roomName, setRoomName] = useState("")
	const [roomDescription, setRoomDescription] = useState("")
	const [defaultCheckInTime, setDefaultCheckInTime] = useState(new Date())
	const [defaultCheckOutTime, setDefaultCheckOutTime] = useState(new Date())
	const [roomLongitude, setRoomLongitude] = useState("")
	const [roomLatitude, setRoomLatitude] = useState("")
	const [roomImage, setRoomImage] = useState("")
	const [loading, setLoading] = useState(true)

	useEffect(() => {
		const keyRef = ref(db, `keyboxes/${boxId}/keys/${keyId}`)
		const handleValue = snapshot => {
			const data = snapshot.val()
			setRoomName(data.name)
			setRoomDescription(data.description)
			setDefaultCheckInTime(new Date(`2000-01-01 ${data.defaultCheckInTime}`))
			setDefaultCheckOutTime(new Date(`2000-01-01 ${data.defaultCheckOutTime}`))
			setRoomLongitude(data.longitude)
			setRoomLatitude(data.latitude)
			setRoomImage(data.image)
			setLoading(false)
			lastReadData = data
		}
		const unsub = onValue(keyRef, handleValue)

		return () => unsub()
	}, [boxId, keyId])

	const save = () => {
		const keyRef = ref(db, `keyboxes/${boxId}/keys/${keyId}`)
        
		set(keyRef, {
			...lastReadData,
			name: roomName,
			description: roomDescription,
			longitude: roomLongitude,
			latitude: roomLatitude,
			image: roomImage,
			defaultCheckInTime: format(defaultCheckInTime, "HH:mm"),
			defaultCheckOutTime: format(defaultCheckOutTime, "HH:mm"),
		})
			.then(() => {
				navigate(`/${boxId}`)
			})
			.catch(error => alert("Something went wrong " + error.message))
	}

	return (
		<EditKeyView
			save={save}
			name={roomName}
			close={() => navigate(`/${boxId}`)}
			back={() => relativeNavigate("../")}
			uid={keyId}
			loading={loading}
		>
			<KeyFormView
				roomName={roomName}
				setRoomName={setRoomName}
				roomDescription={roomDescription}
				setRoomDescription={setRoomDescription}
				roomLongitude={roomLongitude}
				setRoomLongitude={setRoomLongitude}
				roomLatitude={roomLatitude}
				setRoomLatitude={setRoomLatitude}
				roomImage={roomImage}
				setRoomImage={setRoomImage}
				defaultCheckInTime={defaultCheckInTime}
				setDefaultCheckInTime={setDefaultCheckInTime}
				defaultCheckOutTime={defaultCheckOutTime}
				setDefaultCheckOutTime={setDefaultCheckOutTime}
			/>
		</EditKeyView>
	)
}
