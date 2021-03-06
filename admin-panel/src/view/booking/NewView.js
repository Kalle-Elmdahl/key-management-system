

import CircularProgress from "@mui/material/CircularProgress"
import DialogActions from "@mui/material/DialogActions"
import DialogContent from "@mui/material/DialogContent"
import Button from "@mui/material/Button"

import BoxPopupHeader from "../../components/BoxPopupHeader"

import { submitForm } from "../../util/index"

export default function NewBookingView({
	loading,
	close,
	formRef,
    children
}) {
	return (
		<>
			<BoxPopupHeader title="Create new booking" close={close} />
			{loading ? (
				<CircularProgress />
			) : (
				<>
					<DialogContent>
						{children}
					</DialogContent>
					<DialogActions>
						<Button onClick={() => submitForm(formRef)} variant="contained">
							Confirm booking
						</Button>
					</DialogActions>
				</>
			)}
		</>
	)
}
