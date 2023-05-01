//
//  circleImage.swift
//  Landmarks
//
//  Created by Alby on 25/04/23.
//

import SwiftUI

struct circleImage: View {
    
    var image : Image
    
    var body: some View {
        image.clipShape(Circle())
            .clipShape(Circle())
            .overlay{
                Circle().stroke(.green,lineWidth: 4 )
            }
            .shadow(radius: 7)
    }
    
}

struct circleImage_Previews: PreviewProvider {
    static var previews: some View {
        circleImage(image: Image("turtlerock")) //parametric -> we pass turtle rock to the costructor
    }
}
