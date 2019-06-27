import React, { Component } from "react";
import { HashRouter as Router, Link } from "react-router-dom";

export class LogIn extends Component {
  render() {
    return (
      <Router>
        <div
          className="row align-items-center h-100 "
          style={{
            paddingTop: "20px",
            display: "flex",
            justifyContent: "center",
            alignItems: "center"
          }}
        >
          <div
            className="col-md-4 mb-5  align-items-center "
            style={{ paddingTop: "75px" }}
          >
            <div className="card card-login mx-auto mt-5 ">
              <div className="card-header">Register an Account</div>
              <div className="card-body">
                <form>
                  <div className="form-group">
                    <div className="form-row">
                      <div className="col-md-6">
                        <div className="form-label-group">
                          <input
                            type="text"
                            id="firstName"
                            className="form-control"
                            placeholder="First name"
                            required="required"
                            autofocus="autofocus"
                          />
                          <label for="firstName">First name</label>
                        </div>
                      </div>
                      <div className="col-md-6">
                        <div className="form-label-group">
                          <input
                            type="text"
                            id="lastName"
                            className="form-control"
                            placeholder="Last name"
                            required="required"
                          />
                          <label for="lastName">Last name</label>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div className="form-group">
                    <div className="form-label-group">
                      <input
                        type="email"
                        id="inputEmail"
                        className="form-control"
                        placeholder="Email address"
                        required="required"
                      />
                      <label for="inputEmail">Email address</label>
                    </div>
                  </div>
                  <div className="form-group">
                    <div className="form-label-group">
                      <input
                        type="file"
                        id="inputFile"
                        className="form-control"
                        placeholder="Profile Picture"
                      />
                      <label for="inputEmail">Profile Picture</label>
                    </div>
                  </div>
                  <div className="form-group">
                    <div className="form-row">
                      <div className="col-md-6">
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
                      <div className="col-md-6">
                        <div className="form-label-group">
                          <input
                            type="password"
                            id="confirmPassword"
                            className="form-control"
                            placeholder="Confirm password"
                            required="required"
                          />
                          <label for="confirmPassword">Confirm password</label>
                        </div>
                      </div>
                    </div>
                  </div>
                  <a className="btn btn-primary btn-block">Register</a>
                </form>
                <div className="text-center">
                  <Link to="/login" className="d-block small mt-3">
                    Login Page
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
