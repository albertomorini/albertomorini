//
//  ContentView.swift
//  Landmarks
//
//  Created by Alby on 25/04/23.
//

import SwiftUI

struct ContentView: View { //describe the view's content and layout
    var body: some View {
        LandmarkList()
            
    }
}

struct ContentView_Previews: PreviewProvider { //declare the preview
    static var previews: some View {
        ContentView()
    }
}
