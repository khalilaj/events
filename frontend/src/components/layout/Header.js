import React, { Component } from "react";
import Background from "../../../static/frontend/logo.png";
import { HashRouter as Router, Link } from "react-router-dom";

const styles = {
  paperContainer: {
    paddingTop: "75px",
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
      <Router>
        <header
          className="jumbotron my-4 img-fluid bg-image-full text-center text-primary"
          style={styles.paperContainer}
        >
          <h1 className="display-3 mt-0 d-none d-md-block">
            Join the Strathmore Business School Network
          </h1>
          <h3 className="d-none mt-0 d-md-block">
            Discover Events Hosted by Strathmore Business School. Connect and
            make new connections through Strathmore Business School Events
          </h3>
          <div
            className="container d-none mt-0 d-md-block"
            style={{
              paddingTop: "75px",
              paddingBottom: "50px",
              height: "100%",
              display: "flex",
              justifyContent: "center",
              alignItems: "center"
            }}
          >
            <Link to="/register/" className=" btn-lg btn mt-0 btn-primary">
              Register Now
            </Link>
          </div>
        </header>
      </Router>
    );
  }
}

export default Header;
