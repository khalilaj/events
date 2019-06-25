import React, { Component } from "react";

export class UpcomingEventsHeader extends Component {
  render() {
    return (
      <div>
        <div className="row">
          <div className="col-md-8 ">
            <h2>Upcoming Events </h2>
          </div>
          <a className="text-primary navbar-nav ml-auto">View More </a>
        </div>
        <hr className="primary" style={{ borderColor: "1px solid" }} />
      </div>
    );
  }
}

export default UpcomingEventsHeader;
