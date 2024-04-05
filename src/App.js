import logo from "./logo.svg";
import Home from "./Home";
import "./App.css";

import Navbar from "./Navbar";

import React, { Component } from "react";

export default class App extends Component {
  render() {
    console.log("APP loade");
    return (
      <div className="App" style={{ marginTop: "100px" }}>
        <Navbar />
        <Home />
      </div>
    );
  }
}
