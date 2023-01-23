import React, { useState } from "react";
import { useParams } from "react-router-dom";  


export default function Room (){

    const[VoteToSkip, setVoteToSkip] = useState(2);
    const[GuestCanPause, setGuestCanPause] =  useState(false);
    const[isHost, setIsHost] = useState(false);
    
    const{roomCode} = useParams();

    
    fetch('/api/get-room?code='+roomCode)
    .then((response) => response.json())
    .then((data) => {
        
        setVoteToSkip(data.Votes_To_Skip);
        setGuestCanPause(data.Guest_Can_Pause);
        setIsHost(data.Is_Host);
        
    });
    
    return ( 
        <div>
            <h3>{roomCode}</h3>
            <p>Votes: {VoteToSkip}</p>
            <p>Guest Can Pause: {String(GuestCanPause)}</p>
            <p>Host: {String(isHost)}</p>
        </div>
    );

}