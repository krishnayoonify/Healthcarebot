import React, { Component } from "react";
import AppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import logo from "./yoonify-orange-dark.png";
class Navbar extends Component {
  render() {
    console.log("Navbar component rendered");
    return (
      <AppBar
        enableColorOnDark
        position="fixed"
        color="inherit"
        elevation={0}
        sx={{
          bgcolor: "#07172E",
        }}
      >
        <Toolbar>
          <Typography variant="h6" component="div">
            <img
              src={logo}
              alt="Company Logo"
              style={{ height: "70px", marginRight: "10px" }}
            />
          </Typography>
        </Toolbar>
      </AppBar>
    );
  }
}

export default Navbar;
