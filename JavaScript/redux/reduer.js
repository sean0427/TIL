import { combineReducers } from 'redux';
import { READ_BROAD } from '../actions/index';

function updateBoard(state = {}, action) {
    switch (action.type) {
        case READ_BROAD:
            return Object.assign({}, state, {
                data: action.designData
            });
        default:
            return state;
    }
}

export default function broadApp(state = {}, action){
    return {
        data: updateBoard(state.data, action),
    }
};
