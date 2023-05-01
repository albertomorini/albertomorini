//
//  ContentView.swift
//  Landmarks
//
//  Created by Alby on 25/04/23.
//

import SwiftUI

struct ContentView: View { //describe the view's content and layout
    var body: some View {
        
        VStack{
            MapView()
                .ignoresSafeArea(edges: .top)
                .frame(height: 300)
            
            Divider()
            
            circleImage()
                .frame(height:200)
                .offset(y: -130)
                .padding(.bottom,-130)
            
            
            
            VStack(alignment: .leading) {
                Text("Turtle Rock")
                    .font(.title).multilineTextAlignment(.leading).foregroundColor(.green)
                
                HStack {
                    Text("Joshua Tree National Park").font(.subheadline)
                    Spacer() //split at 100% of the screen (right-left)
                    Text("California").foregroundColor(.secondary).font(.subheadline)
                }
            }
            .padding() //give the paddint to entire
            Spacer()
        }
            
    }
}

struct ContentView_Previews: PreviewProvider { //declare the preview
    static var previews: some View {
        ContentView()
    }
}
