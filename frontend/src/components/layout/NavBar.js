import React, { Component } from "react";
import { HashRouter as Router, Link } from "react-router-dom";
import "./layout.css";

export class NavBar extends Component {
  render() {
    return (
      <Router>
        <nav className="navbar navbar-expand-lg navbar-dark bg-primary fixed-top">
          <Link
            to="/"
            className="navbar-brand navbar-nav d-md-block d-none "
            href="#"
          >
            Strathmore Business School Events
          </Link>
          <div className="container">
            <button
              className="navbar-toggler"
              type="button"
              data-toggle="collapse"
              data-target="#navbarResponsive"
              aria-controls="navbarResponsive"
              aria-expanded="false"
              aria-label="Toggle navigation"
            >
              <span className="navbar-toggler-icon" />
            </button>
            <div className="collapse navbar-collapse" id="navbarResponsive">
              <ul className="navbar-nav ml-auto">
                <li className="nav-item ">
                  <Link className="nav-link active" to="/">
                    Home
                    <span className="sr-only">(current)</span>
                  </Link>
                </li>
                <li className="nav-item ">
                  <Link className="nav-link active" to="/event/">
                    Events
                    <span className="sr-only">(current)</span>
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link active" to="/register/">
                    Register
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link active" to="/login/">
                    Login
                  </Link>
                </li>
              </ul>
            </div>
          </div>
        </nav>
      </Router>
    );
  }
}

export default NavBar;
