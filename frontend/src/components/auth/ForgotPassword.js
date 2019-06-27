import React, { Component } from "react";

export class ForgotPassword extends Component {
  render() {
    return (
      <div
        className="row align-items-center h-100"
        style={{
          paddingTop: "75px",
          paddingBottom: "50px",
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
            <div className="card-header">Reset Password</div>

            <div className="card-body">
              <div className="text-center mb-4">
                <h4>Forgot your password?</h4>
                <p>
                  Enter your email address and we will send you instructions on
                  how to reset your password.
                </p>
              </div>

              <form>
                <div className="form-group">
                  <div className="form-label-group">
                    <input
                      type="email"
                      id="inputEmail"
                      class="form-control"
                      placeholder="Enter email address"
                      required="required"
                      autofocus="autofocus"
                    />
                    <label for="inputEmail">Enter email address</label>
                  </div>
                </div>
                <a className="btn btn-primary btn-block" href="login.html">
                  Reset Password
                </a>
              </form>

              <div className="text-center">
                <a className="d-block small mt-3" href="register.html">
                  Register an Account
                </a>
                <a className="d-block small" href="login.html">
                  Login Page
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default ForgotPassword;
