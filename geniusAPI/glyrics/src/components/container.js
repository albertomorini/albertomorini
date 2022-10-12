
import React, { useState } from 'react'; 
import { IonContent, IonSearchbar, IonCard, IonItem, IonIcon, IonLabel, IonButton, IonCardContent } from "@ionic/react";
import axios from "axios";


function Container(props){
    var [suggestion, setSuggestion] = useState("");



    function searchOnGenius(ev) {
        let strQuery = encodeURIComponent(ev.target.value);
        if (strQuery != "") {
            fetch("https://api.genius.com/search?q=strQuery", {
                method: "GET",
                mode: "cors",
                headers:{
                    'Authorization': 'Bearer Fbn65vLE84Ji1Le4hZaZmjXbsUHrvV64ZgLdml3qEcwIMr8z0cPj6dBL8fDy_TJE',
                    'Content-Type': 'application/json',
                },
            }).then(response => {
                console.log(response);
                response.data.response.hits.forEach(singolo => {
                    console.log(singolo);
                })
            }).catch(err => {
                console.log(err);
            });

        } else {

        }
    }

    return(
        <IonContent>
            <IonSearchbar mode="ios" animated="true" showClearButton="focus"  placeholder="Search for a song/artist"
                onIonChange={(ev) => searchOnGenius(ev)}></IonSearchbar>


            <IonCard>
                <IonItem>
                    <IonIcon  slot="start" />
                    <IonLabel>ion-item in a card, icon left, button right</IonLabel>
                    <IonButton fill="outline" slot="end">View</IonButton>
                </IonItem>

                <IonCardContent>
                    This is content, without any paragraph or header tags,
                    within an ion-cardContent element.
                </IonCardContent>
            </IonCard>
        </IonContent>
    )
}

export default Container;