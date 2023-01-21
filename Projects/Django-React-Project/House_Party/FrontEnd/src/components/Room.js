import React, {Component} from 'react';


export default class Room extends Component{

    constructor(props) {
        super(props);
        this.state = {
            VoteToSkip: 2,
            GuestCanPause: false,
            isHost: false,
        };
        this.roomCode = this.props.match.params.roomCode;
        this.GetRoomDetails();
    }

    GetRoomDetails() {
        fetch("/api/get-room" + "?code=" + this.roomCode)
            .then((response) => response.json())
            .then((data) => {
            this.setState({
                VoteToSkip: data.Vote_To_Skip,
                GuestCanPause: data.Guest_Can_Pause,
                isHost: data.is_host,
            });
        });
    }

    render(){
        return ( 
            <div>
                <h3>{this.roomCode}</h3>
                <p>Votes: {this.state.VoteToSkip}</p>
                <p>Guest Can Pause: {this.state.GuestCanPause.toString()}</p>
                <p>Host: {this.state.isHost.toString()}</p>
            </div>
        );
    }
}