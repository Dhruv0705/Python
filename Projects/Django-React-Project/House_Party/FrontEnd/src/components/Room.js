import React, {Component} from 'react';


export default class Room extends Component{

    constructor(props) {
        super(props);
        this.state = {
            VoteToSkip: 2,
            GuestCanPause: false,
            isHost: false,
        };
        this.roomCode.
    }

    render(){

        return ( 
            <div>
                <p>Votes: {this.state.VoteToSkip}</p>
                <p>Guest Can Pause: {this.state.GuestCanPause}</p>
                <p>Host: {this.state.isHost}</p>
            </div>
        );
    };
}