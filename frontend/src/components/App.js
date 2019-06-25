import React, { Component, Fragment } from "react";
import ReactDOM from "react-dom";
import "./App.css";

import Header from "./layout/Header";
import NavBar from "./layout/NavBar";
import Footer from "./layout/Footer";

import UpcomingEvents from "./events/UpcomingEvents";
import UpcomingEventsHeader from "./events/UpcomingEventsHeader";

import { Provider } from "react-redux";
import store from "../store";

class App extends Component {
  render() {
    return (
      <Provider store={store}>
        <div>
          <NavBar />
          <Header />
          <div className="container mt-0">
            <UpcomingEventsHeader />
            <UpcomingEvents />
          </div>
          <Footer />
        </div>
      </Provider>
    );
  }
}

ReactDOM.render(<App />, document.getElementById("app"));
