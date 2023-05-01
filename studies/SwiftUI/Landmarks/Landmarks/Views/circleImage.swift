//
//  circleImage.swift
//  Landmarks
//
//  Created by Alby on 25/04/23.
//

import SwiftUI

struct circleImage: View {
    var body: some View {
        Image("mac.spring")
            .resizable(resizingMode: .stretch)
            .clipShape(Circle())
            .overlay{
                Circle().stroke(.green,lineWidth: 4 )
            }
            .shadow(radius: 7)
    }
    
}

struct circleImage_Previews: PreviewProvider {
    static var previews: some View {
        circleImage()
    }
}
