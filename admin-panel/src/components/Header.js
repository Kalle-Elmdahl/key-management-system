import Toolbar from "@mui/material/Toolbar"
import Box from "@mui/material/Box"
import Menu from "@mui/material/Menu"
import Typography from "@mui/material/Typography"
import Tooltip from "@mui/material/Tooltip"
import IconButton from "@mui/material/IconButton"
import Avatar from "@mui/material/Avatar"
import MenuItem from "@mui/material/MenuItem"
import Paper from "@mui/material/Paper"
import Stack from "@mui/material/Stack"

import { useState } from "react"

import { Link } from "react-router-dom"

const settings = ["Profile", "Account", "Dashboard", "Logout"]

export default function Header() {
	const [anchorElUser, setAnchorElUser] = useState(null)
    
	const handleOpenUserMenu = event => {
		setAnchorElUser(event.currentTarget)
	}

	const handleCloseUserMenu = () => {
		setAnchorElUser(null)
	}

	return (
		<Paper sx={{ px: 2 }} square elevation={1}>
			<Toolbar disableGutters>
                <Box sx={{ flexGrow: 1 }}>
				<Link to={"/"}>
					<Typography variant="h6" noWrap component="div" sx={{ mr: 2 }}>
						LOGO
					</Typography>
				</Link>
                </Box>

				<Stack direction="row" alignItems="center" spacing={2} >
                    <Typography>Logged in as Kalle Elmdahl</Typography>
					<Tooltip title="Open settings">
						<IconButton onClick={handleOpenUserMenu} sx={{ p: 0 }}>
							<Avatar alt="Remy Sharp" src="/static/images/avatar/2.jpg" />
						</IconButton>
					</Tooltip>
					<Menu
						sx={{ mt: "45px" }}
						anchorEl={anchorElUser}
						anchorOrigin={{
							vertical: "top",
							horizontal: "right",
						}}
						keepMounted
						transformOrigin={{
							vertical: "top",
							horizontal: "right",
						}}
						open={Boolean(anchorElUser)}
						onClose={handleCloseUserMenu}
					>
						{settings.map(setting => (
							<MenuItem key={setting} onClick={handleCloseUserMenu}>
								<Typography variant="body1" component="span" textAlign="center">{setting}</Typography>
							</MenuItem>
						))}
					</Menu>
                </Stack>
			</Toolbar>
		</Paper>
	)
}