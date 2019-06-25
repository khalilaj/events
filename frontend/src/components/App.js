import React, { Component, Fragment } from "react";
import ReactDOM from "react-dom";
import './App.css';

import bg from './sbs.png';

const styles = {
    paperContainer: {
        backgroundImage: `url(${bg})`,
        width: '100%',
        height: '400px',
        backgroundSize: 'cover'
    }
};


class App extends Component {
  render() {
    return (
<div>



    <header className="jumbotron my-4 img-fluid bg-image-full text-center text-primary" style={styles.paperContainer}>
    <br />
    <br />
    <br />
    <br />
     <h1 className="display-3">Join the Strathmore Business School Network</h1>
      <h2>Discover Events Hosted by Strathmore Business School. Connect and make new connections through Strathmore Business School Events </h2>
      <a href="#" className="btn btn-primary btn-lg">REGISTER</a>

  </header>
        <br />
  <div className="container">

    <div className="row">
      <div className="col-md-8 mb-5">
        <h2>Upcoming Events </h2>
        <hr/>
      </div>
    </div>

    <div className="row">
      <div className="col-md-4 mb-5">
        <div className="card h-100">
          <img className="card-img-top" src="http://placehold.it/300x200" alt="" />
          <div className="card-body">
            <h4 className="card-title">Card title</h4>
            <p className="card-text">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sapiente esse necessitatibus neque sequi doloribus.</p>
          </div>
          <div className="card-footer text-center">
            <a href="#" className="btn btn-primary">Find Out More!</a>
          </div>
        </div>
      </div>
      <div className="col-md-4 mb-5">
        <div className="card h-100">
          <img className="card-img-top" src="http://placehold.it/300x200" alt="" />
          <div className="card-body">
            <h4 className="card-title">Card title</h4>
            <p className="card-text">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sapiente esse necessitatibus neque sequi doloribus totam ut praesentium aut.</p>
          </div>
          <div className="card-footer text-center">
            <a href="#" className="btn btn-primary">Find Out More!</a>
          </div>
        </div>
      </div>
      <div className="col-md-4 mb-5">
        <div className="card h-100">
          <img className="card-img-top" src="http://placehold.it/300x200" alt="" />
          <div className="card-body">
            <h4 className="card-title ">Card title</h4>
            <p className="card-text">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sapiente esse necessitatibus neque.</p>
          </div>
          <div className="card-footer text-center">
            <a href="#" className="btn btn-primary">Find Out More!</a>
          </div>
        </div>
      </div>
    </div>

  </div>

  <footer className="py-5 bg-primary">
    <div className="container">
      <p className="m-0 text-center text-white">Copyright &copy; SBS EVENTS</p>
    </div>
  </footer>


</div>
    );
  }
}

ReactDOM.render(<App />, document.getElementById("app"));