import React, { Component } from "react";
import MainCard from "./MainCard";
import {
  TextField,
  CircularProgress,
  Card,
  CardContent,
  Typography,
  Grid,
  Divider,
  CardActions,
  Button,
  //   item,
} from "@mui/material";
import Avatar from "@mui/material/Avatar";
import UserIcon from "./219970.png";
export default class Consult extends Component {
  render() {
    return (
      <div>
        <h1>Result</h1>
        <div style={{ overflowY: "auto", height: "75vh" }}>
          <MainCard
            className="card"
            style={{
              minHeight: "100px",
              maxWidth: "500px",
              border: "none",
              backgroundColor: "rgb(255 252 252 / 42%)",
            }}
          >
            <CardContent style={{ padding: 0 }}>
              <div
                style={{
                  display: "flex",
                  justifyContent: "center",
                  marginBottom: "20px",
                  position: "relative",
                }}
              >
                <div>
                  <Avatar
                    alt="test"
                    src={UserIcon} // replace with your user icon image path
                    sx={{
                      width: "80px",
                      height: "80px",
                      border: "2px solid",
                    }}
                  />
                </div>
              </div>
              <Typography
                variant="h5"
                style={{
                  textAlign: "center",
                  marginBottom: "10px",
                  color: "black",
                  fontWeight: "bold",
                }}
              >
                William statham
              </Typography>
              <Typography
                variant="h6"
                style={{
                  textAlign: "center",
                  marginBottom: "10px",
                  color: "#525457",
                  fontSize: "15px",
                }}
              >
                Dermatalogist
              </Typography>
              <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
                enim ad minim veniam, quis nostrud exercitation ullamco laboris
                nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor
                in reprehenderit.s
              </p>
              <CardActions>
                <Button
                  variant="outlined"
                  color="primary"
                  // onClick={() => this.handleViewClick(item.image_url)}
                  align="center"
                  style={{
                    backgroundColor: "#ff6100",
                    color: "#FFFFFF",
                    width: "100%",
                    border: "0",
                  }}
                >
                  Free Consulting
                </Button>
              </CardActions>
            </CardContent>
          </MainCard>
          <MainCard
            className="card"
            style={{
              minHeight: "100px",
              maxWidth: "500px",
              border: "none",
              backgroundColor: "rgb(255 252 252 / 42%)",
              marginTop: "30px",
            }}
          >
            <CardContent style={{ padding: 0 }}>
              <div
                style={{
                  display: "flex",
                  justifyContent: "center",
                  marginBottom: "20px",
                  position: "relative",
                }}
              >
                <div>
                  <Avatar
                    alt="test"
                    src={UserIcon} // replace with your user icon image path
                    sx={{
                      width: "80px",
                      height: "80px",
                      border: "2px solid",
                    }}
                  />
                </div>
              </div>
              <Typography
                variant="h5"
                style={{
                  textAlign: "center",
                  marginBottom: "10px",
                  color: "black",
                  fontWeight: "bold",
                }}
              >
                William statham
              </Typography>
              <Typography
                variant="h6"
                style={{
                  textAlign: "center",
                  marginBottom: "10px",
                  color: "#525457",
                  fontSize: "15px",
                }}
              >
                Dermatalogist
              </Typography>
              <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
                enim ad minim veniam, quis nostrud exercitation ullamco laboris
                nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor
                in reprehenderit.s
              </p>
              <CardActions>
                <Button
                  variant="outlined"
                  color="primary"
                  // onClick={() => this.handleViewClick(item.image_url)}
                  align="center"
                  style={{
                    backgroundColor: "#ff6100",
                    color: "#FFFFFF",
                    width: "100%",
                    border: "0",
                  }}
                >
                  Free Consulting
                </Button>
              </CardActions>
            </CardContent>
          </MainCard>
        </div>
      </div>
    );
  }
}
