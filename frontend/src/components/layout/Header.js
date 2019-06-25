import React, { Component } from "react";
import Background from "../../../static/frontend/logo.png";

const styles = {
  paperContainer: {
    width: "100%",
    height: "400px",
    backgroundSize: "cover",
    backgroundImage:
      "url('https://assets.smartbygep.com/sites/default/files/top-banner/events.jpg')"
  }
};

export class Header extends Component {
  render() {
    return (
      <header
        className="jumbotron my-4 img-fluid bg-image-full text-center text-primary"
        style={styles.paperContainer}
      >
        <h1 className="display-3 mt-0 d-none d-md-block">
          Join the Strathmore Business School Network
        </h1>
        <h3 className="d-none mt-0 d-md-block">
          Discover Events Hosted by Strathmore Business School. Connect and make
          new connections through Strathmore Business School Events
        </h3>
        <a href="#" className="btn mt-0 btn-primary">
          REGISTER
        </a>
      </header>
    );
  }
}

export default Header;
