import React, { Component } from "react";
import { Container, Grid, Typography } from "@mui/material";
import Consult from "./Consult";
import Chatbot from "./Chatbot";
export default class Home extends Component {
  render() {
    console.log("Home component rendered");
    return (
      <div>
        <Container maxWidth="xl">
          {" "}
          {/* xl for extra-large, adjust as needed */}
          <Grid container spacing={2}>
            <Grid item xs={9}>
              <Chatbot />
            </Grid>
            <Grid item xs={3}>
              <Consult />
            </Grid>
          </Grid>
        </Container>
      </div>
    );
  }
}
