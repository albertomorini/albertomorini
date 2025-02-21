const { useState, useEffect } = require("react");

const MyMaps = (props) => {

    const defaultURL = "https://www.openstreetmap.org/export/embed.html?bbox=12.3231719%2C45.8907889%2C12.3231719%2C45.8907889&amp;layer=mapnik" 

    const [OpenMapsURL,setOpenMapsURL] = useState();

    function converterAdd2Coords(civicNr, streetName, city) {
        // https://nominatim.openstreetmap.org/search?q=135+pilkington+avenue,+birmingham&format=json&polygon=1&addressdetails=1
        let address = civicNr + "+" + streetName + ",+" + city
        return fetch("https://nominatim.openstreetmap.org/search?q=" + address + "&format=json&polygon=1&addressdetails=1", {
            method: "GET",
            headers: {
                "Content-type": "Application/JSON"
            }
        }).then(res => res.json()).then(res => {
            return { lat: res[0].lat, lon: res[0].lon };
        })
    }
    async function generateURLmap(civicNr, streetName, city) {
        let cords = await converterAdd2Coords(civicNr, streetName, city);
        let tmp = "https://www.openstreetmap.org/export/embed.html?bbox=" + cords.lon + "%2C" + cords.lat + "%2C" + cords.lon + "%2C" + cords.lat + "&amp;layer=mapnik";
        return 
    }
    
    useEffect(()=>{
        let urlMap = await generateURLmap(props.civicNr, props.streetName, props.city);
        setOpenMapsURL(urlMap);
    },[]);

    return(
        <div>
            <iframe width="425" height="350"
                src={(OpenMapsURL != null) ? OpenMapsURL :defaultURL}
                style={{border: "1px solid black", borderRadius: "5px"}}
            />
        </div>
    )
}

default export MyMaps;