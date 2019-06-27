import React, { Component } from "react";
import EventList from "./EventList";
import { HashRouter as Router, Link } from "react-router-dom";

export class Event extends Component {
  render() {
    return (
      <Router>
        <div className="container">
          <h2
            className=" text-primary text-center"
            style={{
              paddingTop: "75px"
            }}
          >
            All Events{" "}
          </h2>

          <hr className="bg-primary" style={{ borderColor: "50px solid" }} />
          <EventList />
        </div>
      </Router>
    );
  }
}

export default Event;
