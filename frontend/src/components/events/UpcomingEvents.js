import React, { Component } from "react";

export class Footer extends Component {
  render() {
    return (
      <div className="row">
        <div className="col-md-4 mb-5">
          <div className="card h-100">
            <img
              className="card-img-top"
              src="https://scontent.fnbo2-1.fna.fbcdn.net/v/t1.0-9/64812121_2469763869753037_8053428249708986368_n.jpg?_nc_cat=111&_nc_ht=scontent.fnbo2-1.fna&oh=f11c95c597faef70033704b1b1b33767&oe=5D790C66"
              alt=""
            />
            <div className="card-body">
              <h4 className="card-title">
                Business Management Skill Programme
              </h4>
              <p className="card-text">
                Aimed at equipping SME contractors with relevant and practical
                business management skills, to become competitive, as a result
                have better chances of winning contracts in public sector road
                construction projects.
              </p>
            </div>
            <div className="card-footer text-center">
              <a href="#" className="btn btn-primary">
                Register Now
              </a>
            </div>
          </div>
        </div>
        <div className="col-md-4 mb-5">
          <div className="card h-100">
            <img
              className="card-img-top"
              src="https://scontent.fnbo2-1.fna.fbcdn.net/v/t1.0-9/61959850_2438169849579106_1919721330429657088_n.png?_nc_cat=103&_nc_ht=scontent.fnbo2-1.fna&oh=5e5c73658a3487ba3c2d0328796faa13&oe=5D8662A7"
              alt=""
            />
            <div className="card-body">
              <h4 className="card-title">Public Key Executive Programme</h4>
              <p className="card-text">
                This course is designed to enable middle and senior level
                personnel develop policy implementation schemes that deliver
                results.
              </p>
            </div>
            <div className="card-footer text-center">
              <a href="#" className="btn btn-primary">
                Register Now
              </a>
            </div>
          </div>
        </div>
        <div className="col-md-4 mb-5">
          <div className="card h-100">
            <img
              className="card-img-top"
              src="https://scontent.fnbo2-1.fna.fbcdn.net/v/t1.0-9/61594917_2431534510242640_2239662833107206144_n.png?_nc_cat=103&_nc_ht=scontent.fnbo2-1.fna&oh=90b4fc1ca579b557afedfaf945eb718e&oe=5D897F3F"
              alt=""
            />
            <div className="card-body">
              <h4 className="card-title ">Effective Directore Class</h4>
              <p className="card-text">
                The programme is designed for experienced board directors who
                are interested in staying up to date with the latest development
                in their board roles. It takes a deeper dive into strategy, risk
                and financial implications.
              </p>
            </div>
            <div className="card-footer text-center">
              <a href="#" className="btn btn-primary">
                Register Now
              </a>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default Footer;
