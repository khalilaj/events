import React, { Component } from "react";
import { HashRouter as Router, Link } from "react-router-dom";
import EventList from "../events/EventList";

export class UpcomingEvents extends Component {
  render() {
    return (
      <Router>
        <div className="container">
          <div className="row">
            <div className="col-8">
              <h2 className=" text-primary">Upcoming Events </h2>
            </div>
            <div className="col-4">
              <Link
                to="/event/"
                className=" text-white navbar-nav ml-auto btn  btn-primary "
              >
                View More{" "}
              </Link>
            </div>
          </div>
          <div>
            <hr className="bg-primary" style={{ borderColor: "10px solid" }} />
          </div>
          <EventList />
        </div>
      </Router>
    );
  }
}

export default UpcomingEvents;
