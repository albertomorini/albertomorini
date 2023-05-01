//
//  Landmark.swift
//  Landmarks
//
//  Created by Alby on 30/04/23.
//

import Foundation
import SwiftUI
import CoreLocation


struct Landmark: Hashable, Codable { //Codable -> makes easier to move data between the structure and data file

    var id: Int

    var name: String

    var park: String

    var state: String

    var description: String

    
    
    private var imageName : String
    var image: Image{
        Image(imageName)
    }
    
    
    private var coordinates: Coordinates
    
    var locationCoordinate: CLLocationCoordinate2D{
        CLLocationCoordinate2D(
            latitude: coordinates.lat ,
            longitude: coordinates.lon
        )
    }
    
    struct Coordinates: Hashable,Codable{
        var lat: Double
        var lon: Double
    }
}
