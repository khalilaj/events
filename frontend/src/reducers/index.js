import { combineReducers } from "redux";
import event from "./event";
import errors from "./errors";
import messages from "./messages";

export default combineReducers({
  event,
  messages,
  errors
});
