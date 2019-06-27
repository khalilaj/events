import React, { Component } from "react";
import ReactDOM from "react-dom";

import {
  HashRouter as Router,
  Route,
  Switch,
  Redirect
} from "react-router-dom";

import "./App.css";

import Home from "./layout/Home";
import NavBar from "./layout/NavBar";
import Footer from "./layout/Footer";

import Event from "./events/Event";
import LogIn from "./auth/LogIn";
import Register from "./auth/Register";
import ForgotPassword from "./auth/ForgotPassword";

import { Provider } from "react-redux";
import store from "../store";

class App extends Component {
  render() {
    return (
      <Provider store={store}>
        <div>
          <NavBar />
          <div className="container mt-0">
            <Router>
              <Route exact path="/" component={Home} />
              <Route exact path="/event" component={Event} />
              <Route exact path="/register" component={Register} />
              <Route exact path="/login" component={LogIn} />
              <Route exact path="/forgotpassword" component={ForgotPassword} />
            </Router>
          </div>
          <Footer />
        </div>
      </Provider>
    );
  }
}

ReactDOM.render(<App />, document.getElementById("app"));
