#### Data Protection & Privacy Term Project - Incognito: Efficient Full-Domain K-Anonymity
#### Team Members:
<ul>
  <li>Tolgahan Dayanıklı - S5674594</li>
  <li>Sahel Riazi - </li>
  <li>Ergi Toshkezi -</li>
</ul>
 
# Incognito-Algorithm

## Background Information
<p>The necessity to safeguard individual privacy and the growing importance of data in decision-making processes have brought approaches to efficiently and effectively anonymize data to the forefront of research. This work explores the complexities of k-anonymization, a well-known technique to guarantee data anonymity, concentrating on the novel idea of multi-dimensional recoding. We investigate both single-dimensional and multidimensional models while analyzing various methods of data generalization and suppression, from partition-based models to models based on hierarchies. This effort culminates in the development of a reliable and scalable multi-dimensional data model through an examination of prior research and its respective advantages. </p>

## Introduction
<p>The volume of data being gathered, processed, and shared in the digital era is at an all-time high. Datasets offer priceless insights that fuel societal progress in a variety of industries, including healthcare and e-commerce. However, enormous responsibility comes along with great data. The necessity to protect someone's privacy while making sure that the datasets are still useful for study and analysis is inherent. Data anonymization techniques have developed and evolved as a result of this conflict.
</p>
<br>
<p>In order to ensure that every person in the released dataset cannot be identified from at least k-1 other people, K-anonymization has emerged as a possible solution to the conundrum. Although this approach is valid in theory, it has had difficulty being put into practice, especially when used with large and varied datasets. By thoroughly examining the available k-anonymization models and techniques, our study aims to tackle these difficulties head-on. In this study, we provide a multi-dimensional data model that effectively achieves k-anonymity and a taxonomy that classifies the wide range of current anonymization methods. With the goal of advancing the dialogue on data privacy, this initiative offers practical solutions that are both effective and efficient.
</p>

## Dataset Selection and Why this Dataset is selected?
<p>The contentious discussion over tragic interactions with police emphasizes the urgent need for data-driven insights to promote openness, enhance laws, and spur societal change. The significance of safeguarding individuals' privacy inside these datasets cannot be emphasized, especially when dealing with such a delicate subject, as the world grows more and more data-centric. Our study makes use of k-anonymization's potential to secure the moral application of a vast dataset documenting fatalities during police encounters from 2015 to 2017. We hope to establish a new benchmark for reconciling the pursuit of knowledge with the supreme value of individual privacy by employing multi-dimensional recoding and diverse anonymization models.</p>
<p>Our database contains a thorough list of people who unfortunately perished after interactions with the police between the beginning of 2015 and the end of 2017. The following attributes make up the dataset's structure:
</p>
<ul>
  <li>ID: A unique identifier for each record.</li>
  <li>Name: Name of the deceased.</li>
  <li>Date: Date of death.</li>
  <li>Manner of Death: Method by which death occurred.</li>
  <li>Armed: Denotes the type of armament, if any, that the individual had at the time of the encounter.</li>
  <li>Age: Age of the deceased.</li>
  <li>Gender: Gender classification (M for Male, W for Female).</li>
  <li>Race: Categorized racial identifiers (e.g., B for Black, W for White, A for Asian, etc.).</li>
  <li>State: The U.S. state where the encounter took place.</li>
  <li>Signs of Mental Illness: A binary attribute indicating the presence (True) or absence (False) of signs of mental illness.</li>
  <li>Threat Level: Classification of the perceived threat posed by the individual during the encounter.</li>
  <li>Flee: Describes if the individual was attempting to flee the scene or not.</li>
</ul>
<p> 
  Important Notice: This dataset offers academics the possibility to find potential systemic problems or biases by helping them understand the patterns and circumstances behind these sad incidents. However, because of its in-depth nature, it also raises significant privacy issues, necessitating the use of cutting-edge data anonymization techniques.
</p>

### Objectives to Study:

<ol>
 <li>Data Understanding:</li>
  <ul>
    <li>To fully comprehend the dataset in terms of its properties, potential security holes in it, and range of values.</li>
    <li>To identify quasi-identifiers in the dataset that might be exploited in linkage attacks to reveal personal data about specific people.</li>
  </ul>
  <li>Privacy Preservation Using K-anonymization:</li>
  <ul>
    <li>
      To use the k-anonymization principles to prevent the unique identification of every individual data point inside the dataset, protecting user privacy.
    </li>
    <li>To investigate multi-dimensional recoding techniques with the goal of achieving privacy protection while maintaining the usefulness of data.</li>
  </ul>
  <li>Model Evaluation:</li>
  <ul>
    <li>To evaluate several k-anonymization models presented in the research critically, taking into account the benefits of local versus global recoding models.</li>
    <li>In order to maintain the integrity of the dataset, it is necessary to measure the information loss caused by each anonymization model and to make sure that this loss stays within acceptable bounds.</li>
  </ul>
  <li>Data Utility Retention:</li>
  <ul>
    <li>To guarantee that the resulting data maintains its analytical usefulness while protecting personal identities.</li>
    <li>In order to avoid losing important insights into police contacts, it is important to assess how the k-anonymization procedure affects the capacity to spot patterns within the data.</li>
  </ul>
</ol>






