/*
See LICENSE folder for this sample’s licensing information.

Abstract:
A view showing the list of landmarks.
*/

import SwiftUI

struct ContentView: View { //declare the behaviour
    var body: some View {
        LandmarkList() //we call the LandmarkList 
    }
}

struct ContentView_Previews: PreviewProvider { //declare the preview
    static var previews: some View {
        ContentView()
    }
}
