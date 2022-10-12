import { IonContent, IonHeader, IonPage, IonTitle, IonToolbar } from '@ionic/react';
import  Container from '../components/container';
import './Home.css';

const Home: React.FC = () => {
  return (
    <IonPage>
      <IonHeader>
        <IonToolbar mode="ios">
          <IonTitle>Glyrics</IonTitle>
        </IonToolbar>
      </IonHeader>
      <IonContent fullscreen>
        <IonHeader collapse="condense">
          <IonToolbar>
            <IonTitle size="large">Glyrics</IonTitle>
          </IonToolbar>
        </IonHeader>
        <Container />
      </IonContent>
    </IonPage>
  );
};

export default Home;
