# Data Science Fallacies (to avoid)


A list of common data science fallacies to avoid.

I'll explain **the fallacies** and add an *example*.

Language: 
- 🇬🇧 English
- 🇮🇹 Italian 

-----


## Cherry Picking

**eng:** Is picking a slice of data that fit the claim ignoring the bigger picture or the data that bring us different results.
Usually ignoring the entire dataset.

>*eg*: *We can't tell the global warming is fake just because in the last 5 years the temperature hasn't raised... We have to elaborate all data* (having a dataset of more than 5 years)

**ita:** Viene selezionata solo una partizione di dati, in modo da favorire una tesi, ignorando o nascondendo valori che potrebbero darci torto.
Spesso ignorando l'intero set di dati.

*eg*: *Non possiamo dire che il riscaldamento globale sia falso solo perché negli ultimi 5 anni la temperatura non è salita... Dobbiamo elaborare tutti i dati* (avendo un dataset contenente più di 5 anni)






## Sampling Bias

**eng**: Creating an assumption based on a favorite/unfavorite sample of the entire dataset.

*eg*: *we survey how many university students listen to hip/hop by asking it in a classroom.. We can't assume that x% of university students like hip/hop because we have sample just a class and not the entire university*

**ita**: Si crea un'assuzione basta su un campione favorito/sfavorito dell'intera popolazione.

*es*:*sondiamo a quanti studenti universitari piaccia l'hip/hop chiedendolo in un'aula.. Non possiamo assumere che a x% degli studenti univesitari piaccia l'hip/hop perché abbiamo chiesto a una sola classe e non all'intera università*


## Regression towards the mean

**eng**: When we assume something based on a past event.
*eg*:*A basketball team wins the championship, the next year we can't assume it will win again, even if has a top coach etc., because in the long run there are a lot of other factors (drug scandals of players etc.)*

**it**: Quando assumiamo qualcosa basandoci su un evento del passato.
*es*:*Una squadra di basket vince un campionato, il prossimo anno non possiamo assumere che vincerà di nuovo, seppur ha un coach bravissimo etc., perché alla lunga ci sono tanti altri fattori (scandali legati dalla droga dei giocatori, etc.)*

## Overfitting

**eng**: When a model is too faithful/close to the test dataset and probably will fail on another dataset.

**it**: Quando un modello è troppo fedele/legato al dataset di test, quindi potrebbe fallire con un altro dataset.


## Data dredging (p-hacking/data snooping)

**eng**: forcing a correlation of two different hypothesis basing on the similarity of the dataset.
*eg*: *Number of people that like HipHop is the same number of people who's like icecream... No correlation between these two hypothesis, but if we have a dataset with similar numbers we (wrongly) assume it*

*it*: forzare una correlazione di due ipotesi diverse basandosi sulla somiglianza dei dati.
*it*: *Numero di persone a cui piace l'HipHop è lo stesso di quello a cui piace il gelato... Non vi è correlazione tra le due ipotesi, ma se abbiamo un sataset con una somiglianza dei numeri, potremmo (erroneamente) forzare la teoria*


## False Casuality

**eng**: assuming that two event apparently tied are incluenced between each other or one is the cause of another. 
*eg*: *after installed a new software your pc crash, so you assume that the program is the cause... Which could be possible, but we can't be sure of that (eg. faulty component, crappy operating system like windows, etc.)*

**it**: assumere che due eventi apparantemente correlati siano influenzati o l'uno la causa dell'altro.
*es*: *dopo aver installato un nuovo software il tuo pc va in cresh, quindi assumi sia colpa di quel programma... Cosa possibile, ma non possiamo esserne certi (es. componenti fisici difettosi, sistema operativo scadente come windows, etc.)*

## GAMBLER'S FALLACY (or Monte Carlo Fallacy)
My fav.

**ENG**: When an event is happening so often in the past events so you think that on the next round will happen with a lower probability (or viceversa)... But probability is indipendent of past events
*eg*:*You toss a coin for three times, and all the times it landed on 'head' so you (wrongly) thing that the next toss 'head' will be less likely to land (but the probability is indipendent of the past event)*

**IT**: *Quando un evento sta accadendo spesso negli eventi passati, quindi pensi che nel prossimo round avrà una probabilità minore (o viceversa).. Ma la probabilità è indipendente dagli esiti passati*
*es*:*Tirando una moneta per 3 volte, esce tutte le volte 'testa', quindi tu (erroneamente) pensi che alla 4th volta testa avrà probabilità minore*


## SIMSPON'S PARADOX

**ENG**: When a trend shows up on different subset of a dataset, but disappear or viceversa when the groups are combinated
*eg*: *On an univesity's application the percentage of ammission is 41% (of 12,763 people), which are 44% (of 8,442) males and for females there's a percentage of 35% (of 4,321).... 44 and 35 are closer to 41 but way off compared gender to gender.*


## PUBLICATION BIAS
**ENG**:Interesting research findings are more likely to be published, distorting our impression of reality
*eg*:*Is hard to make an example, but I'll try: You make a suvery about the favourites music genre and the last question is how old are the people. Next, you find that all the people which has answered to the survey are between 21 and 22 years old; so you (wrongly) don't publish this info, distorting the reality (because probably older people likes a different genre)*

## SURVIVORSHIP BIAS
**ENG**:Drawing a conlcusion from an incomplete set of data, becuase the data 'survived' some selection criteria
*eg*: *A war aircraft come back home after a battle, full of bullet holes everywhere except on the engine, so you decide to armour the places where the plane has shotted because no airplane came with bullet home on the engine... But is just luck of not being hitted on the engine (you should put armour there too)*
*eg2*: *3 of 5 university students have the best grades, you find out that those 3 students has been on the same high school... So you think that high school has a very good education.. But you should take a larger sample of students*

## GERRYMANDERING
**ENG**: Manilupating the "geographical" boundaries used to group data in order to change the result.
*eg*: *We have a dataset of 20 people, voting for red or for black. Next we have to divide the dataset making group of 5 people.. Changing the boundaries we can totally change the result, event with very different numbers (8for black and 12 for red)* 


## HAWTRONE EFFECT
**ENG**: The act of monitoring someone can affect their behaviour, also know as the Observer Effect.
*eg*: *A boss observs his employer, whose feeling the pressure make some mistakes on their job*


## MCNAMARA FALLACY
**ENG**: When in complex situation you draw a conclusion just looking the data and not other facts.
*eg* : *In a war, the Pusha's army kills 800k soldier of Drake's army, which one kills just a 100k of enemy's army... Anyway, Drake wins the war, because he has conquest the Pusha's headquarter with just two soldier.*


