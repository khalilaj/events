import React, { Component } from "react";
import { connect } from "react-redux";
import { PropTypes } from "prop-types";
import { HashRouter as Router, Link } from "react-router-dom";

import { getEvent, deleteEvent } from "../../actions/event";

class EventList extends Component {
  static PropPropTypesTypes = {
    event: PropTypes.array.isRequired,
    getEvent: PropTypes.func.isRequired,
    deleteEvent: PropTypes.func.isRequired
  };
  componentDidMount() {
    this.props.getEvent();
    console.log(this.props.event);
  }
  render() {
    return (
      <Router>
        <div className="container">
          <div className="row" style={{ marginTop: "50px" }}>
            {this.props.event.map(ev => (
              <div className="col-lg-4 col-sm-6 mb-4" key={ev.id}>
                <div className="card h-100">
                  <Link to="/register/">
                    <img
                      style={{ height: "300px" }}
                      className="card-img-top"
                      src={ev.event_image}
                      alt="http://placehold.it/700x400"
                    />
                  </Link>
                  <div className="card-body">
                    <h4 className="card-title">
                      <Link to="/register/">{ev.event_name}</Link>
                    </h4>
                    <p className="card-text">{ev.event_description}</p>
                  </div>
                  <div className="card-footer text-center">
                    <Link to="/register/" className="btn btn-primary">
                      Register Now
                    </Link>
                  </div>
                </div>
              </div>
            ))}
          </div>

          <ul className="pagination justify-content-center">
            <li className="page-item">
              <a className="page-link" href="#" aria-label="Previous">
                <span aria-hidden="true">&laquo;</span>
                <span className="sr-only">Previous</span>
              </a>
            </li>
            <li className="page-item">
              <a className="page-link" href="#">
                1
              </a>
            </li>
            <li className="page-item">
              <a className="page-link" href="#">
                2
              </a>
            </li>
            <li className="page-item">
              <a className="page-link" href="#">
                3
              </a>
            </li>
            <li className="page-item">
              <a className="page-link" href="#" aria-label="Next">
                <span aria-hidden="true">&raquo;</span>
                <span className="sr-only">Next</span>
              </a>
            </li>
          </ul>
        </div>
      </Router>
    );
  }
}
const mapStateToProps = state => ({
  event: state.event.event
});

export default connect(
  mapStateToProps,
  { getEvent, deleteEvent }
)(EventList);
