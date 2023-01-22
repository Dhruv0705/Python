import React, {Component, useState } from "react";
import { Button, Grid, Typography, TextField, FormHelperText, FormControl, FormControlLabel, RadioGroup, Radio } from "@mui/material";
import { FilePresent } from "@mui/icons-material";
import { useNavigate, Link } from "react-router-dom";


export default class CreateRoomPage extends Component {
    
    DefaultVotes = 2;

    constructor(props) {
        super(props);
        this.state = {
            GuestCanPause: true,
            VotesToSkip: this.DefaultVotes,
        };

        this.HandleRoomButtonPressed = this.HandleRoomButtonPressed.bind(this);
        this.HandleVotesChanged = this.HandleVotesChanged.bind(this);
        this.HandleGuestCanPauseChange = this.HandleGuestCanPauseChange.bind(this);
    }
    

    HandleVotesChanged(e){
        this.setState({
            VotesToSkip: e.target.value,
        });
    }

    HandleGuestCanPauseChange(e){
        this.setState({
            GuestCanPause: e.target.value === "true" ? true : false,
        });
    }

    HandleRoomButtonPressed(){
        var csrftoken = getCookie('csrftoken');
        const requestOptions = {
            method: "POST",
            headers: {"content-Type": "application/json",  'X-CSRFToken': csrftoken},
            body: JSON.stringify({
                Votes_To_Skip: this.state.VotesToSkip,
                Guest_Can_Pause: this.state.GuestCanPause,
            }),
        };
        fetch("/api/create-room", requestOptions)
            .then((response) => response.json())
            .then((data) => console.log(data));
    }

    render() {
        return (

            <Grid container spacing={1}>
                <Grid item xs={12} align="center">
                    <Typography component="h4" variant="h4">Create A Room</Typography>
                 </Grid>
                 <Grid item xs={12} align="center">
                    <FormControl component="fieldset">
                        <FormHelperText>
                            <Typography component= "span" variant="body2" align="center">Guest Control of Playback State</Typography>
                        </FormHelperText>
                        <RadioGroup row defaultValue="true" onChange={this.HandleGuestCanPauseChange}>
                            <FormControlLabel 
                                value="true" 
                                label="Play/Pause"
                                labelPlacement="bottom"
                                control={<Radio color="primary"/>}
                            />
                            <FormControlLabel
                                value="false"
                                label="No Control"
                                labelPlacement="bottom"
                                control={<Radio color="secondary"/>}
                            />
                        </RadioGroup>
                    </FormControl>
                </Grid>
                <Grid item xs={12} align="center">
                    <FormControl>
                        <TextField 
                            required={true} 
                            type="number" 
                            onChange={this.HandleVotesChanged}
                            defaultValue={this.DefaultVotes} 
                            inputProps={{ min:1, style:{textAlign:"center"}, }} 
                        />
                        <FormHelperText>
                            <Typography component= "span" variant="body2" align="center">Votes Required To Skip Songs</Typography>
                        </FormHelperText>
                    </FormControl>
                </Grid>
                <Grid item xs={12} align="center">
                    <Button color="primary" variant="contained" onClick={this.HandleRoomButtonPressed}>Create A Room</Button>
                </Grid>
                <Grid item xs={12} align="center">
                    <Button color="secondary" variant="contained" to="/" component={Link}>Back</Button>
                </Grid>
            </Grid>
        );
    }
}