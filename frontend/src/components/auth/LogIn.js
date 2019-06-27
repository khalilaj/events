import React, { Component } from "react";

import { HashRouter as Router, Link } from "react-router-dom";

export class LogIn extends Component {
  render() {
    return (
      <Router>
        <div
          className="row align-items-center h-100"
          style={{
            paddingTop: "75px",
            paddingBottom: "25px",
            height: "100%",
            display: "flex",
            justifyContent: "center",
            alignItems: "center"
          }}
        >
          <div
            className="col-md-4 mb-5  align-items-center "
            style={{ paddingTop: "75px" }}
          >
            <div className="card card-login mx-auto mt-5 h-100">
              <div className="card-header">Login</div>
              <div className="card-body">
                <form>
                  <div className="form-group">
                    <div className="form-label-group">
                      <input
                        type="email"
                        id="inputEmail"
                        className="form-control"
                        placeholder="Email address"
                        required="required"
                        autofocus="autofocus"
                      />
                      <label for="inputEmail">Email address</label>
                    </div>
                  </div>
                  <div className="form-group">
                    <div className="form-label-group">
                      <input
                        type="password"
                        id="inputPassword"
                        className="form-control"
                        placeholder="Password"
                        required="required"
                      />
                      <label for="inputPassword">Password</label>
                    </div>
                  </div>
                  <div className="form-group">
                    <div className="checkbox">
                      <label>
                        <input type="checkbox" value="remember-me" /> Remember
                        Password
                      </label>
                    </div>
                  </div>
                  <a className="btn btn-primary btn-block" href="index.html">
                    Login
                  </a>
                </form>

                <div className="text-center">
                  <Link to="/register" className="d-block small mt-3">
                    Register an Account
                  </Link>
                  <Link to="/forgotpassword" className="d-block small">
                    Forgot Password?
                  </Link>
                </div>
              </div>
            </div>
          </div>
        </div>
      </Router>
    );
  }
}

export default LogIn;
