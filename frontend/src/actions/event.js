import axios from "axios";

import { createMessage, returnErrors } from "./messages";

import {
  GET_EVENT,
  DELETE_EVENT,
  ADD_EVENT,
  PUT_EVENT,
  GET_ERRORS
} from "./types";

//GET EVENT
export const getEvent = () => dispatch => {
  axios
    .get("/api/event")
    .then(res => {
      dispatch({
        type: GET_EVENT,
        payload: res.data
      });
    })
    .catch(err => console.log(err));
};

//DELETE EVENT
export const deleteEvent = id => dispatch => {
  axios
    .delete(`/api/==event/${id}/`)
    .then(res => {
      dispatch(createMessage({ deleteEvent: "Event Deleted" }));
      dispatch({
        type: DELETE_EVENT,
        payload: id
      });
    })
    .catch(err => console.log(err));
};

//PUT EVENT
export const putEvent = (event, id) => dispatch => {
  axios.put(
    `/api/leads/${id}/`,
    event
      .then(res => {
        dispatch({
          type: PUT_EVENT,
          payload: res.data
        });
      })
      .catch(err => console.log(err))
  );
};

//ADD EVENT
export const addEvent = event => dispatch => {
  axios
    .post("/api/event/", event)
    .then(res => {
      dispatch(createMessage({ addEvent: "Event Added" }));
      dispatch({
        type: ADD_EVENT,
        payload: res.data
      });
    })
    .catch(err => {
      const errors = {
        msg: err.response.data,
        status: err.response.status
      };
      dispatch({
        type: GET_ERRORS,
        payload: errors
      });
    });
};
