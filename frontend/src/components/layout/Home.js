import React, { Component } from "react";

import UpcomingEvents from "../events/UpcomingEvents";
import Header from "../layout/Header";

export class Home extends Component {
  render() {
    return (
      <div style={{ width: "100%" }}>
        <Header />
        <UpcomingEvents />
      </div>
    );
  }
}

export default Home;
