import {
  GET_EVENT,
  DELETE_EVENT,
  ADD_EVENT,
  PUT_EVENT
} from "../actions/types";

const initialState = {
  event: []
};

export default function(state = initialState, action) {
  switch (action.type) {
    case GET_EVENT:
      return {
        ...state,
        event: action.payload.event
      };
    case DELETE_EVENT:
      return {
        ...state,
        event: state.event.filter(lead => event.id !== action.payload)
      };
    case ADD_EVENT:
      return {
        ...state,
        event: [...state.event, action.payload]
      };
    case PUT_EVENT:
      return {
        ...state,
        event: [...state.event, action.payload]
      };
    default:
      return state;
  }
}
