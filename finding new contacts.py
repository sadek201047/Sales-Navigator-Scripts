import os
import csv
import time
import winsound
import requests
from bs4 import BeautifulSoup
html_source = '''<ul>
      <li class="list-style-none">
        <div id="ember11193" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/steve-chirhart-3726275/" id="ember11194" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember11195" class="presence-entity presence-entity--size-5 ember-view"><img alt="Steve Chirhart" id="ember11196" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4E03AQGHhJ4M_5q2fQ/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=pwFszgNym2u1GwN3pODoYBAmRRhnjNl6EczudK_A7Gk">

<div id="ember11197" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/steve-chirhart-3726275/" id="ember11198" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Steve Chirhart
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Creative Director, Social Media &amp; Copywriting
    </span>
</a>    <time class="time-badge time-ago">
      Connected 53 minutes ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember11199" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Steve Chirhart" data-ember-action="" data-ember-action-11200="11200">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Steve Chirhart
      </span>

    </button>

<div id="ember11797" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember11201" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember11202" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Steve Chirhart"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember11203" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember11204" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-11205="11205">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Steve Chirhart from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember11206" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember11208" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/rafael-soriano-75b22612/" id="ember11209" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember11210" class="presence-entity presence-entity--size-5 ember-view"><img alt="Rafael Soriano" id="ember11211" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5603AQFGJirH1Z3lNA/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=uMdMBlWZq8uoirHS9hMBvi2QsQMh7_FLJziLFPSsbRM">

<div id="ember11212" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/rafael-soriano-75b22612/" id="ember11213" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Rafael Soriano
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Associate Creative Director
    </span>
</a>    <time class="time-badge time-ago">
      Connected 3 hours ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember11214" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Rafael Soriano" data-ember-action="" data-ember-action-11215="11215">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Rafael Soriano
      </span>

    </button>

<div id="ember11857" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember11216" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember11217" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Rafael Soriano"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember11218" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember11219" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-11220="11220">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Rafael Soriano from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember11221" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember11223" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/stephanie-luna-40b1a011a/" id="ember11224" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember11225" class="presence-entity presence-entity--size-5 ember-view"><img alt="Stephanie Luna" id="ember11226" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5103AQE0XwyOY2T9jA/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=C4o5AsXuW0HFr6CAWCrMA11MCPt7fzurOjhMkzcIJeQ">

<div id="ember11227" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/stephanie-luna-40b1a011a/" id="ember11228" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Stephanie Luna
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Studio Stylist at The RealReal
    </span>
</a>    <time class="time-badge time-ago">
      Connected 5 hours ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember11229" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Stephanie Luna" data-ember-action="" data-ember-action-11230="11230">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Stephanie Luna
      </span>

    </button>

<div id="ember11861" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember11231" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember11232" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Stephanie Luna"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember11233" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember11234" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-11235="11235">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Stephanie Luna from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember11236" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember11238" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/theweave/" id="ember11239" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember11240" class="presence-entity presence-entity--size-5 ember-view"><img alt="Rob Weaver" id="ember11241" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5603AQHFCjqj8Gzu5w/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=50wmhjnnGoetm1FI6bODRsmi9S9Sn82FeGmj4_6Bdsc">

<div id="ember11242" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/theweave/" id="ember11243" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Rob Weaver
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Art Director at Wunderman
    </span>
</a>    <time class="time-badge time-ago">
      Connected 7 hours ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember11244" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Rob Weaver" data-ember-action="" data-ember-action-11245="11245">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Rob Weaver
      </span>

    </button>

<div id="ember11858" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember11246" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember11247" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Rob Weaver"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember11248" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember11249" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-11250="11250">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Rob Weaver from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember11251" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember11253" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/john-pluska-3814a320/" id="ember11254" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember11255" class="presence-entity presence-entity--size-5 ember-view"><img alt="John Pluska" id="ember11256" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4D03AQEDua1yA9r9WA/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=YXC3lXVxxWyUapa7I3KypCBnboUx11QrasYv5BQnlVI">

<div id="ember11257" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/john-pluska-3814a320/" id="ember11258" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      John Pluska
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Soft Goods Photographer/Photography Manager
    </span>
</a>    <time class="time-badge time-ago">
      Connected 7 hours ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember11259" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to John Pluska" data-ember-action="" data-ember-action-11260="11260">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to John Pluska
      </span>

    </button>

<div id="ember11860" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember11261" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember11262" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for John Pluska"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember11263" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember11264" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-11265="11265">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove John Pluska from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember11266" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember11268" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/julianadacosta/" id="ember11269" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember11270" class="presence-entity presence-entity--size-5 ember-view"><img alt="Juliana da Costa" id="ember11271" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4D03AQEkqvtLRci2CA/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=vIIMF3n9PSEgmyMqRzkTDGckHJ_Zr3yITqUTUZQA3Qk">

<div id="ember11272" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/julianadacosta/" id="ember11273" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Juliana da Costa
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Senior Designer at Kroger / Art Director and Owner at Toca.Design
    </span>
</a>    <time class="time-badge time-ago">
      Connected 9 hours ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember11274" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Juliana da Costa" data-ember-action="" data-ember-action-11275="11275">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Juliana da Costa
      </span>

    </button>

<div id="ember11859" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember11276" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember11277" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Juliana da Costa"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember11278" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember11279" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-11280="11280">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Juliana da Costa from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember11281" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember11283" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/kiana-alvarez-449844b8/" id="ember11284" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember11285" class="presence-entity presence-entity--size-5 ember-view"><img alt="Kiana Alvarez" id="ember11286" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5603AQGYV1p7IDkUXg/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=tPyubl-DZE6dAHP_WurvSghPWZGRaWi18mozN6ID7TA">

<div id="ember11287" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/kiana-alvarez-449844b8/" id="ember11288" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Kiana Alvarez
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Senior Photo Editor at Lulus.com
    </span>
</a>    <time class="time-badge time-ago">
      Connected 10 hours ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember11289" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Kiana Alvarez" data-ember-action="" data-ember-action-11290="11290">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Kiana Alvarez
      </span>

    </button>

<div id="ember11864" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember11291" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember11292" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Kiana Alvarez"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember11293" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember11294" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-11295="11295">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Kiana Alvarez from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember11296" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember11298" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/jessienalake/" id="ember11299" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember11300" class="presence-entity presence-entity--size-5 ember-view"><img alt="Jessiena Lake" id="ember11301" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4E03AQG1GQGUmLOP9w/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=hOHIeG7ITryXkH75pIiWH0XFpPfJHjK9WTTNvUrhILQ">

<div id="ember11302" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/jessienalake/" id="ember11303" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Jessiena Lake
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Commercial Photographer at Jessiena Lake
    </span>
</a>    <time class="time-badge time-ago">
      Connected 12 hours ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember11304" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Jessiena Lake" data-ember-action="" data-ember-action-11305="11305">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Jessiena Lake
      </span>

    </button>

<div id="ember11798" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember11306" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember11307" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Jessiena Lake"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember11308" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember11309" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-11310="11310">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Jessiena Lake from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember11311" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember11313" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/erin-white-33819342/" id="ember11314" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember11315" class="presence-entity presence-entity--size-5 ember-view"><img alt="Erin White" id="ember11316" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5603AQHwin4N6fCmUw/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=l9oxVWQdj5n9hIDOZ5MUcbp2AbgGmlATLN67tmtCIMs">

<div id="ember11317" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/erin-white-33819342/" id="ember11318" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Erin White
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Studio Manager at Amazon
    </span>
</a>    <time class="time-badge time-ago">
      Connected 13 hours ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember11319" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Erin White" data-ember-action="" data-ember-action-11320="11320">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Erin White
      </span>

    </button>

<div id="ember11863" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember11321" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember11322" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Erin White"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember11323" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember11324" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-11325="11325">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Erin White from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember11326" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember11328" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/eugenedp/" id="ember11329" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember11330" class="presence-entity presence-entity--size-5 ember-view"><img alt="Eugene du Plessis" id="ember11331" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5603AQF6fg5KkJTHVA/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=oCi8T1ZmKtf6WkJsOwn429f5k_PZ0IVvFVj5BzLXMpc">

<div id="ember11332" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/eugenedp/" id="ember11333" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Eugene du Plessis
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Experience strategist with a passion for design thinking
    </span>
</a>    <time class="time-badge time-ago">
      Connected 14 hours ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember11334" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Eugene du Plessis" data-ember-action="" data-ember-action-11335="11335">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Eugene du Plessis
      </span>

    </button>

<div id="ember11862" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember11336" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember11337" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Eugene du Plessis"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember11338" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember11339" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-11340="11340">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Eugene du Plessis from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember11341" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember11343" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/denitsa-komitska-84645141/" id="ember11344" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember11345" class="presence-entity presence-entity--size-5 ember-view"><img alt="Denitsa Komitska" id="ember11346" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5603AQGgKqkitT1ihg/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=44n5e0xCqTzRFz-baWYFdvyvDa5QaIWZRqkiVeFnPZ8">

<div id="ember11347" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/denitsa-komitska-84645141/" id="ember11348" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Denitsa Komitska
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Studio Manager at A NEAT TOUCH STUDIO LIMITED
    </span>
</a>    <time class="time-badge time-ago">
      Connected 15 hours ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember11349" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Denitsa Komitska" data-ember-action="" data-ember-action-11350="11350">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Denitsa Komitska
      </span>

    </button>

<div id="ember11865" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember11351" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember11352" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Denitsa Komitska"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember11353" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember11354" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-11355="11355">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Denitsa Komitska from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember11356" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember11358" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/laura-mellor-0a12b172/" id="ember11359" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember11360" class="presence-entity presence-entity--size-5 ember-view"><img alt="LAURA MELLOR" id="ember11361" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4E03AQGByg79thTq-Q/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=XuQ-uowtF-fxU6S3oZgcZoxFe0vvX6eddfLRUHXMso4">

<div id="ember11362" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/laura-mellor-0a12b172/" id="ember11363" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      LAURA MELLOR
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Studio  &amp; Project Manger
    </span>
</a>    <time class="time-badge time-ago">
      Connected 16 hours ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember11364" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to LAURA MELLOR" data-ember-action="" data-ember-action-11365="11365">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to LAURA MELLOR
      </span>

    </button>

<div id="ember11866" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember11366" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember11367" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for LAURA MELLOR"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember11368" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember11369" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-11370="11370">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove LAURA MELLOR from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember11371" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember11373" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/malou-burger/" id="ember11374" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember11375" class="presence-entity presence-entity--size-5 ember-view"><img alt="Malou Burger" id="ember11376" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5603AQE4wgO19SPCgg/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=gUqAZj70H-qXeuHKlYLtiKc09ZSgaBgGh66Bo_-M-EU">

<div id="ember11377" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/malou-burger/" id="ember11378" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Malou Burger
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Food Photographer &amp; Director ★ Stills ★ Motion ★ Food ★ Drink ★ Portraits ★ Lifestyle ★ Creating beautiful photographs to sell food and increase sales.
    </span>
</a>    <time class="time-badge time-ago">
      Connected 16 hours ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember11379" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Malou Burger" data-ember-action="" data-ember-action-11380="11380">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Malou Burger
      </span>

    </button>

<div id="ember11799" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember11381" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember11382" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Malou Burger"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember11383" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember11384" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-11385="11385">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Malou Burger from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember11386" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember11388" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/mattcarrphoto/" id="ember11389" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember11390" class="presence-entity presence-entity--size-5 ember-view"><img alt="Matt Carr" id="ember11391" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5603AQGU1pDXak-bIw/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=EC0vv8aZw-MWyMnt1hiNpPt-ZoqtD5kALvLYAuvZ2Cg">

<div id="ember11392" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/mattcarrphoto/" id="ember11393" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Matt Carr
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Fashion Photographer at HSN
    </span>
</a>    <time class="time-badge time-ago">
      Connected 21 hours ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember11394" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Matt Carr" data-ember-action="" data-ember-action-11395="11395">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Matt Carr
      </span>

    </button>

<div id="ember11872" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember11396" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember11397" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Matt Carr"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember11398" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember11399" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-11400="11400">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Matt Carr from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember11401" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember11403" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/amanda-rice-924604134/" id="ember11404" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember11405" class="presence-entity presence-entity--size-5 ember-view"><img alt="Amanda Rice" id="ember11406" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5603AQEvx0I-BoBzpA/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=r0xLwYDss2m4KJmWhNPNkyl7USrO50xTP_gNVEx2EOs">

<div id="ember11407" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/amanda-rice-924604134/" id="ember11408" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Amanda Rice
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Administrator Certification at Trailhead by Salesforce
    </span>
</a>    <time class="time-badge time-ago">
      Connected 21 hours ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember11409" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Amanda Rice" data-ember-action="" data-ember-action-11410="11410">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Amanda Rice
      </span>

    </button>

<div id="ember11867" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember11411" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember11412" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Amanda Rice"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember11413" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember11414" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-11415="11415">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Amanda Rice from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember11416" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember11418" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/ambraisse/" id="ember11419" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember11420" class="presence-entity presence-entity--size-5 ember-view"><img alt="Thierry Ambraisse" id="ember11421" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5603AQEa8UU6cGynew/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=1_u7se4HgCNuoJcyv5TCAQU7rZnS8f03WbnGnJtGxEo">

<div id="ember11422" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/ambraisse/" id="ember11423" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Thierry Ambraisse
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Director, Nike Global Digital Design — Studio
    </span>
</a>    <time class="time-badge time-ago">
      Connected 22 hours ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember11424" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Thierry Ambraisse" data-ember-action="" data-ember-action-11425="11425">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Thierry Ambraisse
      </span>

    </button>

<div id="ember11868" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember11426" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember11427" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Thierry Ambraisse"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember11428" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember11429" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-11430="11430">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Thierry Ambraisse from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember11431" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember11433" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/cassidy-iwersen-a207a07/" id="ember11434" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember11435" class="presence-entity presence-entity--size-5 ember-view"><img alt="Cassidy Iwersen" id="ember11436" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5603AQFAheF2lBELkA/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=0DYhZeRd4cHG30q2Yef8gLKfInL-YNT9h5uPR7LeBPc">

<div id="ember11437" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/cassidy-iwersen-a207a07/" id="ember11438" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Cassidy Iwersen
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Sr. Art Director, Home at Target
    </span>
</a>    <time class="time-badge time-ago">
      Connected 22 hours ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember11439" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Cassidy Iwersen" data-ember-action="" data-ember-action-11440="11440">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Cassidy Iwersen
      </span>

    </button>

<div id="ember11870" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember11441" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember11442" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Cassidy Iwersen"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember11443" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember11444" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-11445="11445">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Cassidy Iwersen from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember11446" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember11448" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/emil-sinanagic-b48ba629/" id="ember11449" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember11450" class="presence-entity presence-entity--size-5 ember-view"><img alt="Emil Sinanagic" id="ember11451" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4D03AQFxhFBGNqJu5w/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=W4d0bQXmfwJvI4slSpiCJhSaQtMNYbj-40OtP47zzhQ">

<div id="ember11452" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/emil-sinanagic-b48ba629/" id="ember11453" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Emil Sinanagic
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Fashion Photographer at Represented by: Creative Space Artist MGMT
    </span>
</a>    <time class="time-badge time-ago">
      Connected 23 hours ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember11454" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Emil Sinanagic" data-ember-action="" data-ember-action-11455="11455">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Emil Sinanagic
      </span>

    </button>

<div id="ember11869" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember11456" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember11457" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Emil Sinanagic"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember11458" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember11459" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-11460="11460">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Emil Sinanagic from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember11461" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember11463" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/matelli-graves-9182b2145/" id="ember11464" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember11465" class="presence-entity presence-entity--size-5 ember-view"><img alt="Matelli Graves" id="ember11466" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4E03AQFKY9jy1ivZgA/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=vHWCDhGLfzog4TP3YXnARVYFZbB88RNzpN6lrb-sC_s">

<div id="ember11467" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/matelli-graves-9182b2145/" id="ember11468" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Matelli Graves
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Freelance Photographer | Videographer at Matelli Graves Media
    </span>
</a>    <time class="time-badge time-ago">
      Connected 23 hours ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember11469" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Matelli Graves" data-ember-action="" data-ember-action-11470="11470">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Matelli Graves
      </span>

    </button>

<div id="ember11871" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember11471" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember11472" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Matelli Graves"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember11473" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember11474" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-11475="11475">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Matelli Graves from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember11476" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember11478" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/jessie-lane-313317b/" id="ember11479" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember11480" class="presence-entity presence-entity--size-5 ember-view"><img alt="Jessie Lane" id="ember11481" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4E03AQHobTDjZRSzlA/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=QCgzSbDs-AbvZN32n5zIwi_ZYDHrLBjEihgoWffjQrs">

<div id="ember11482" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/jessie-lane-313317b/" id="ember11483" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Jessie Lane
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Senior Producer | Brand Marketing | Creative Ops
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 day ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember11484" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Jessie Lane" data-ember-action="" data-ember-action-11485="11485">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Jessie Lane
      </span>

    </button>

<div id="ember11873" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember11486" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember11487" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Jessie Lane"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember11488" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember11489" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-11490="11490">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Jessie Lane from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember11491" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember11493" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/khaled-abdelnasser-934044a4/" id="ember11494" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember11495" class="presence-entity presence-entity--size-5 ember-view"><img alt="khaled abdelnasser" id="ember11496" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4E03AQFfV0A_k5_98w/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=hdp6y70ZH_hyBvMnzufXFZy5GaO1gfIjimqy9w2bnH8">

<div id="ember11497" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/khaled-abdelnasser-934044a4/" id="ember11498" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      khaled abdelnasser
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Operation engineer at  The Arabian company for oils &amp; derivatives
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 day ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember11499" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to khaled abdelnasser" data-ember-action="" data-ember-action-11500="11500">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to khaled abdelnasser
      </span>

    </button>

<div id="ember11875" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember11501" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember11502" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for khaled abdelnasser"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember11503" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember11504" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-11505="11505">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove khaled abdelnasser from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember11506" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember11508" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/richard-anderson-26130717/" id="ember11509" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember11510" class="presence-entity presence-entity--size-5 ember-view"><img alt="Richard Anderson" id="ember11511" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4D03AQG8DwR2wKl7OA/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=OlK9PSyangvZ1KmwBF8SQeOx8aq44QklWxLrqYzsIbE">

<div id="ember11512" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/richard-anderson-26130717/" id="ember11513" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Richard Anderson
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Studio Manager / Senior Designer - Poggenpohl
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 day ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember11514" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Richard Anderson" data-ember-action="" data-ember-action-11515="11515">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Richard Anderson
      </span>

    </button>

<div id="ember11874" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember11516" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember11517" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Richard Anderson"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember11518" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember11519" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-11520="11520">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Richard Anderson from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember11521" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember11523" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/tyler-marie-shumpert-17bb8810a/" id="ember11524" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember11525" class="presence-entity presence-entity--size-5 ember-view"><img alt="Tyler Marie Shumpert" id="ember11526" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5603AQEhZ6yazHZlKw/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=YxZMrNbDegue3pHutuOQ12uB9vuk9o_VTHeibNXDM44">

<div id="ember11527" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/tyler-marie-shumpert-17bb8810a/" id="ember11528" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Tyler Marie Shumpert
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Department Manager of Women's Contemporary and Activewear  at Von Maur
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 day ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember11529" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Tyler Marie Shumpert" data-ember-action="" data-ember-action-11530="11530">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Tyler Marie Shumpert
      </span>

    </button>

<div id="ember11876" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember11531" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember11532" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Tyler Marie Shumpert"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember11533" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember11534" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-11535="11535">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Tyler Marie Shumpert from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember11536" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember11538" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/erin-beatty-9a479612/" id="ember11539" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember11540" class="presence-entity presence-entity--size-5 ember-view"><img alt="Erin Beatty" id="ember11541" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4D03AQFzDoIpGBSPtA/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=7jj4737t7p0gQa8UF20HjsyMNJ5WQf6gRx6EflWe66s">

<div id="ember11542" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/erin-beatty-9a479612/" id="ember11543" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Erin Beatty
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Creative Director 
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 day ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember11544" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Erin Beatty" data-ember-action="" data-ember-action-11545="11545">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Erin Beatty
      </span>

    </button>

<div id="ember11878" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember11546" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember11547" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Erin Beatty"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember11548" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember11549" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-11550="11550">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Erin Beatty from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember11551" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember11553" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/bonjourlaura/" id="ember11554" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember11555" class="presence-entity presence-entity--size-5 ember-view"><img alt="Laura Ross" id="ember11556" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4D03AQHho-816eHKTA/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=oA0929aNhnFxCfHLvCdrU3sXagVTRN3G2W8xiDg7feE">

<div id="ember11557" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/bonjourlaura/" id="ember11558" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Laura Ross
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Producer
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 day ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember11559" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Laura Ross" data-ember-action="" data-ember-action-11560="11560">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Laura Ross
      </span>

    </button>

<div id="ember11800" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember11561" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember11562" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Laura Ross"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember11563" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember11564" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-11565="11565">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Laura Ross from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember11566" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember11568" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/tris314/" id="ember11569" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember11570" class="presence-entity presence-entity--size-5 ember-view"><img alt="Tristan Petts" id="ember11571" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4D03AQGiPp7ZiindVA/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=wPQJD3nlD-Jm3so357zh3lP41EnqQHd20iYgWmOhTco">

<div id="ember11572" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/tris314/" id="ember11573" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Tristan Petts
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Photographer at Next Group PLC
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 day ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember11574" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Tristan Petts" data-ember-action="" data-ember-action-11575="11575">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Tristan Petts
      </span>

    </button>

<div id="ember11877" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember11576" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember11577" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Tristan Petts"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember11578" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember11579" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-11580="11580">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Tristan Petts from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember11581" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember11583" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/ellaclbartlett/" id="ember11584" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember11585" class="presence-entity presence-entity--size-5 ember-view"><img alt="Ella Bartlett" id="ember11586" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4D03AQFRxouMeyQClw/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=oyVyz0t14DvXxzERxFNvNseGeHjhmv0pO9eohEN1moA">

<div id="ember11587" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/ellaclbartlett/" id="ember11588" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Ella Bartlett
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Producer at Creative Drive
    </span>
</a>    <time class="time-badge time-ago">
      Connected 2 days ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember11589" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Ella Bartlett" data-ember-action="" data-ember-action-11590="11590">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Ella Bartlett
      </span>

    </button>

<div id="ember11880" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember11591" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember11592" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Ella Bartlett"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember11593" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember11594" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-11595="11595">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Ella Bartlett from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember11596" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember11598" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/joanna-mcclure-653b306/" id="ember11599" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember11600" class="presence-entity presence-entity--size-5 ember-view"><img alt="Joanna McClure" id="ember11601" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4E03AQHH9fSup6c0BA/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=Hp8wHP7eECTXBRSamhCcXnKbAjt4Q5Nln--ORQRDW6E">

<div id="ember11602" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/joanna-mcclure-653b306/" id="ember11603" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Joanna McClure
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Photographer
    </span>
</a>    <time class="time-badge time-ago">
      Connected 2 days ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember11604" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Joanna McClure" data-ember-action="" data-ember-action-11605="11605">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Joanna McClure
      </span>

    </button>

<div id="ember11879" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember11606" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember11607" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Joanna McClure"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember11608" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember11609" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-11610="11610">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Joanna McClure from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember11611" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember11613" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/ben-koch-68900383/" id="ember11614" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember11615" class="presence-entity presence-entity--size-5 ember-view"><img alt="Ben Koch" id="ember11616" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5603AQE_nFzVksac6A/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=1DUv8ThD3ZniTFtqspTRrh0o9pIpD3sJkpVF5Xck1v0">

<div id="ember11617" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/ben-koch-68900383/" id="ember11618" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Ben Koch
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Assistant Photography Manager at Sports Direct, Flannels &amp; House of Fraser
    </span>
</a>    <time class="time-badge time-ago">
      Connected 2 days ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember11619" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Ben Koch" data-ember-action="" data-ember-action-11620="11620">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Ben Koch
      </span>

    </button>

<div id="ember11801" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember11621" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember11622" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Ben Koch"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember11623" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember11624" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-11625="11625">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Ben Koch from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember11626" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember11628" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/mattrainone/" id="ember11629" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember11630" class="presence-entity presence-entity--size-5 ember-view"><img alt="Matt Rainone" id="ember11631" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4E03AQFWMuqtzZTLzw/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=I-tb2xBNIrHI6CSchVUX8gn1oGaiXKotT7fYT_sb7rE">

<div id="ember11632" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/mattrainone/" id="ember11633" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Matt Rainone
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      I'm actually working in my second career choice. When I was 10, I wanted to be a professional sports mascot.
    </span>
</a>    <time class="time-badge time-ago">
      Connected 2 days ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember11634" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Matt Rainone" data-ember-action="" data-ember-action-11635="11635">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Matt Rainone
      </span>

    </button>

<div id="ember11881" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember11636" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember11637" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Matt Rainone"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember11638" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember11639" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-11640="11640">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Matt Rainone from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember11641" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember11643" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/cheryl-carpenter-2a9b8020/" id="ember11644" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember11645" class="presence-entity presence-entity--size-5 ember-view"><img alt="Cheryl Carpenter" id="ember11646" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4D03AQFDp0_IwyFhDQ/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=8NFFXNYQB88JBpm2RIpo5D416xtqJBFvbZ2MvQahQCQ">

<div id="ember11647" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/cheryl-carpenter-2a9b8020/" id="ember11648" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Cheryl Carpenter
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      International multi-award winning Kitchen + Bath designer
    </span>
</a>    <time class="time-badge time-ago">
      Connected 2 days ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember11649" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Cheryl Carpenter" data-ember-action="" data-ember-action-11650="11650">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Cheryl Carpenter
      </span>

    </button>

<div id="ember11882" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember11651" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember11652" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Cheryl Carpenter"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember11653" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember11654" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-11655="11655">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Cheryl Carpenter from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember11656" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember11658" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/katelyn-lichtenwalner-450134a4/" id="ember11659" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember11660" class="presence-entity presence-entity--size-5 ember-view"><img alt="Katelyn Lichtenwalner" id="ember11661" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5603AQHcjVISxttT2Q/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=DoYxTDWURox0VExVo00U6_UGRPGD3PmjmJLycUTy3fw">

<div id="ember11662" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/katelyn-lichtenwalner-450134a4/" id="ember11663" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Katelyn Lichtenwalner
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Studio Manager at Straub Collaborative, Inc
    </span>
</a>    <time class="time-badge time-ago">
      Connected 3 days ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember11664" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Katelyn Lichtenwalner" data-ember-action="" data-ember-action-11665="11665">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Katelyn Lichtenwalner
      </span>

    </button>

<div id="ember11883" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember11666" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember11667" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Katelyn Lichtenwalner"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember11668" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember11669" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-11670="11670">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Katelyn Lichtenwalner from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember11671" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember11673" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/ola-ekerhov-64221a22/" id="ember11674" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember11675" class="presence-entity presence-entity--size-5 ember-view"><img alt="Ola Ekerhov" id="ember11676" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4D03AQH-h09kh2G9WQ/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=NfC7FHsTBb8z5C0ES3b_WTYkLEH0zC2EG2lIr78lrMY">

<div id="ember11677" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/ola-ekerhov-64221a22/" id="ember11678" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Ola Ekerhov
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Director Of Ecommerce at Acne Studios AB
    </span>
</a>    <time class="time-badge time-ago">
      Connected 3 days ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember11679" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Ola Ekerhov" data-ember-action="" data-ember-action-11680="11680">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Ola Ekerhov
      </span>

    </button>

<div id="ember11884" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember11681" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember11682" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Ola Ekerhov"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember11683" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember11684" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-11685="11685">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Ola Ekerhov from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember11686" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember11688" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/sami-hajar/" id="ember11689" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember11690" class="presence-entity presence-entity--size-5 ember-view"><img alt="Sami Hajar" id="ember11691" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4D03AQHcQXnygF3kHA/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=7jlqnxr-23Zld3NPbIzf1TS5XYrOsQUW8dNrSZzhFu4">

<div id="ember11692" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/sami-hajar/" id="ember11693" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Sami Hajar
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Creative Director at INKED Magazine
    </span>
</a>    <time class="time-badge time-ago">
      Connected 3 days ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember11694" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Sami Hajar" data-ember-action="" data-ember-action-11695="11695">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Sami Hajar
      </span>

    </button>

<div id="ember11802" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember11696" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember11697" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Sami Hajar"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember11698" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember11699" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-11700="11700">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Sami Hajar from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember11701" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember11703" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/jdelacr/" id="ember11704" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember11705" class="presence-entity presence-entity--size-5 ember-view"><img alt="Jon&amp;#39;Dell Delacruz" id="ember11706" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5603AQF4rfe06_pTJg/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=wSgpedHfztR5wH3WzSzrk61oqsR5JhqjkjZp6lum-2Y">

<div id="ember11707" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/jdelacr/" id="ember11708" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Jon'Dell Delacruz
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Associate Art Director
    </span>
</a>    <time class="time-badge time-ago">
      Connected 3 days ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember11709" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Jon&amp;#39;Dell Delacruz" data-ember-action="" data-ember-action-11710="11710">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Jon'Dell Delacruz
      </span>

    </button>

<div id="ember11803" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember11711" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember11712" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Jon&amp;#39;Dell Delacruz"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember11713" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember11714" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-11715="11715">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Jon&amp;#39;Dell Delacruz from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember11716" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember11718" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/rosalizjimenez9/" id="ember11719" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember11720" class="presence-entity presence-entity--size-5 ember-view"><img alt="Rosaliz Jimenez" id="ember11721" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4E03AQG369V17D4q8A/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=6QOk47TEVoLmlTxMSwrHSrRUxAmlz4mLOLzQfxku3vA">

<div id="ember11722" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/rosalizjimenez9/" id="ember11723" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Rosaliz Jimenez
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Director of Fashion and Photography at Dia&amp;Co.
    </span>
</a>    <time class="time-badge time-ago">
      Connected 3 days ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember11724" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Rosaliz Jimenez" data-ember-action="" data-ember-action-11725="11725">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Rosaliz Jimenez
      </span>

    </button>

<div id="ember11804" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember11726" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember11727" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Rosaliz Jimenez"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember11728" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember11729" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-11730="11730">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Rosaliz Jimenez from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember11731" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember11733" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/ethanflaeger/" id="ember11734" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember11735" class="presence-entity presence-entity--size-5 ember-view"><img alt="Ethan Flaeger" id="ember11736" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5603AQH6QFS1TQlTHw/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=X8pPyEQcQZ9_mXo16NKsQXPnnT9_Pd_OLWjGEGu6rfc">

<div id="ember11737" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/ethanflaeger/" id="ember11738" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Ethan Flaeger
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Sr. Project / Program / Ops Manager - Creative &amp; Digital
    </span>
</a>    <time class="time-badge time-ago">
      Connected 3 days ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember11739" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Ethan Flaeger" data-ember-action="" data-ember-action-11740="11740">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Ethan Flaeger
      </span>

    </button>

<div id="ember11885" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember11741" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember11742" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Ethan Flaeger"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember11743" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember11744" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-11745="11745">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Ethan Flaeger from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember11746" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember11748" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/eman-hussein-73335949/" id="ember11749" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember11750" class="presence-entity presence-entity--size-5 ember-view"><img alt="eman hussein" id="ember11751" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5603AQGXA4Y-v-6rhQ/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=YqZFvWpm8W-O8hX_IwsNlFEHFk8TTt8Wm0jr6U-3AVg">

<div id="ember11752" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/eman-hussein-73335949/" id="ember11753" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      eman hussein
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      E-commerce agent at Costco Wholesale
    </span>
</a>    <time class="time-badge time-ago">
      Connected 4 days ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember11754" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to eman hussein" data-ember-action="" data-ember-action-11755="11755">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to eman hussein
      </span>

    </button>

<div id="ember11886" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember11756" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember11757" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for eman hussein"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember11758" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember11759" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-11760="11760">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove eman hussein from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember11761" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember11763" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/joy-coakley/" id="ember11764" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember11765" class="presence-entity presence-entity--size-5 ember-view"><img alt="Joy Coakley (Goldin)" id="ember11766" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5603AQGOLWsurfhkQQ/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=W7IE8kL10Zm6RpVlQajmMVaUK6-AKc6Ff87ZLXvdBK0">

<div id="ember11767" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/joy-coakley/" id="ember11768" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Joy Coakley (Goldin)
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Photographer/Stylist at Joy Coakley
    </span>
</a>    <time class="time-badge time-ago">
      Connected 4 days ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember11769" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Joy Coakley (Goldin)" data-ember-action="" data-ember-action-11770="11770">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Joy Coakley (Goldin)
      </span>

    </button>

<div id="ember11805" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember11771" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember11772" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Joy Coakley (Goldin)"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember11773" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember11774" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-11775="11775">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Joy Coakley (Goldin) from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember11776" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember11778" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/ginai-liverman-5514822b/" id="ember11779" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember11780" class="presence-entity presence-entity--size-5 ember-view"><img alt="Ginai Liverman" id="ember11781" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5603AQFX4l27_n4X8g/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=PuGKnqXT40-IqQq61sJdaZVEgeKf0xqMJBgb8JlKkuI">

<div id="ember11782" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/ginai-liverman-5514822b/" id="ember11783" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Ginai Liverman
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Manager of Studio Operations, Macy's  Inc.
    </span>
</a>    <time class="time-badge time-ago">
      Connected 4 days ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember11784" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Ginai Liverman" data-ember-action="" data-ember-action-11785="11785">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Ginai Liverman
      </span>

    </button>

<div id="ember11887" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember11786" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember11787" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Ginai Liverman"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember11788" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember11789" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-11790="11790">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Ginai Liverman from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember11791" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember11890" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/rosannatalarico/" id="ember11891" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember11892" class="presence-entity presence-entity--size-5 ember-view"><img alt="Rosanna Talarico" id="ember11893" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4E03AQHExWtkSMWTnQ/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=bxp-_GCinscQcJKSr9bpyuYTdLj10V21ZrGF8rbwJh4">

<div id="ember11894" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/rosannatalarico/" id="ember11895" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Rosanna Talarico
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Studio Ops. Coordinator, Fashion Studio at Macy's
    </span>
</a>    <time class="time-badge time-ago">
      Connected 4 days ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember11896" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Rosanna Talarico" data-ember-action="" data-ember-action-11897="11897">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Rosanna Talarico
      </span>

    </button>

<div id="ember12489" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember11898" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember11899" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Rosanna Talarico"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember11900" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember11901" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-11902="11902">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Rosanna Talarico from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember11903" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember11905" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/thijs-huizer-b71154126/" id="ember11906" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember11907" class="presence-entity presence-entity--size-5 ember-view"><img alt="Thijs Huizer" id="ember11908" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5603AQGCocYYuoG4AA/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=HtTUu16h704rDrWpgvDn_s7l28o7B6J3ZuT1UbhRI-U">

<div id="ember11909" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/thijs-huizer-b71154126/" id="ember11910" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Thijs Huizer
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Freelance Photographer | Dancer | Choreographer | Model 
    </span>
</a>    <time class="time-badge time-ago">
      Connected 4 days ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember11911" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Thijs Huizer" data-ember-action="" data-ember-action-11912="11912">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Thijs Huizer
      </span>

    </button>

<div id="ember12495" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember11913" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember11914" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Thijs Huizer"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember11915" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember11916" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-11917="11917">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Thijs Huizer from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember11918" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember11920" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/dianewahzuercher/" id="ember11921" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember11922" class="presence-entity presence-entity--size-5 ember-view"><img alt="Diane Wah - Zuercher" id="ember11923" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5603AQFw4jgIMmDHnw/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=Pe9FcFiIdUo3g36_Zz0xYOSrR4NvEwCjzO8A8aKEQ0E">

<div id="ember11924" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/dianewahzuercher/" id="ember11925" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Diane Wah - Zuercher
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Photographer and Project Manager
    </span>
</a>    <time class="time-badge time-ago">
      Connected 4 days ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember11926" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Diane Wah - Zuercher" data-ember-action="" data-ember-action-11927="11927">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Diane Wah - Zuercher
      </span>

    </button>

<div id="ember12494" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember11928" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember11929" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Diane Wah - Zuercher"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember11930" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember11931" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-11932="11932">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Diane Wah - Zuercher from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember11933" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember11935" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/alex-waber-1a646b32/" id="ember11936" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember11937" class="presence-entity presence-entity--size-5 ember-view"><img alt="Alex Waber" id="ember11938" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5603AQGGl2uiUvHMMg/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=wdBWWmHpOr6nakaEevLBUqOgGLDqnZffdGjtCjUVarY">

<div id="ember11939" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/alex-waber-1a646b32/" id="ember11940" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Alex Waber
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Commercial and Editorial Photographer.
    </span>
</a>    <time class="time-badge time-ago">
      Connected 4 days ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember11941" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Alex Waber" data-ember-action="" data-ember-action-11942="11942">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Alex Waber
      </span>

    </button>

<div id="ember12497" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember11943" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember11944" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Alex Waber"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember11945" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember11946" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-11947="11947">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Alex Waber from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember11948" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember11950" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/dyland/" id="ember11951" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember11952" class="presence-entity presence-entity--size-5 ember-view"><img alt="Dylan Dawson" id="ember11953" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5603AQG-QrwSQCBW2w/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=sXXyYNf4IahpqEGydeffrSM7SASjHgKLMyrDsV7mzCs">

<div id="ember11954" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/dyland/" id="ember11955" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Dylan Dawson
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Creative Operations Manager
    </span>
</a>    <time class="time-badge time-ago">
      Connected 4 days ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember11956" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Dylan Dawson" data-ember-action="" data-ember-action-11957="11957">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Dylan Dawson
      </span>

    </button>

<div id="ember12496" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember11958" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember11959" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Dylan Dawson"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember11960" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember11961" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-11962="11962">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Dylan Dawson from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember11963" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember11965" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/christine-fitzsimonds-b918716/" id="ember11966" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember11967" class="presence-entity presence-entity--size-5 ember-view"><img alt="Christine Fitzsimonds" id="ember11968" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4E03AQEJRnHVGCfi1w/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=4OfnoWQR_nH2qdw8hyb9Xl4GSoOSSu3T1ynTR9iDljE">

<div id="ember11969" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/christine-fitzsimonds-b918716/" id="ember11970" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Christine Fitzsimonds
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Director Application Development, User Experience  at Aetna
    </span>
</a>    <time class="time-badge time-ago">
      Connected 4 days ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember11971" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Christine Fitzsimonds" data-ember-action="" data-ember-action-11972="11972">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Christine Fitzsimonds
      </span>

    </button>

<div id="ember12498" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember11973" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember11974" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Christine Fitzsimonds"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember11975" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember11976" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-11977="11977">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Christine Fitzsimonds from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember11978" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember11980" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/anis-mulani-987066113/" id="ember11981" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember11982" class="presence-entity presence-entity--size-5 ember-view"><img alt="anis mulani" id="ember11983" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5603AQG4LWg22o9NyQ/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=G1nSCy_Vl6ZuIdd135gs8UgNiOHttekmzENoXSRT61o">

<div id="ember11984" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/anis-mulani-987066113/" id="ember11985" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      anis mulani
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      photo operations editor at Zocdoc
    </span>
</a>    <time class="time-badge time-ago">
      Connected 4 days ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember11986" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to anis mulani" data-ember-action="" data-ember-action-11987="11987">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to anis mulani
      </span>

    </button>

<div id="ember12499" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember11988" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember11989" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for anis mulani"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember11990" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember11991" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-11992="11992">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove anis mulani from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember11993" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember11995" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/nicolasbec/" id="ember11996" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember11997" class="presence-entity presence-entity--size-5 ember-view"><img alt="Nicolas Bernal" id="ember11998" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4E03AQHMG6Eq8leAiQ/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=-iScll_K5v0YiA9hpA4s-Pnb7Loilqkw6wLMLY7JB5Q">

<div id="ember11999" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/nicolasbec/" id="ember12000" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Nicolas Bernal
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Creative Director
    </span>
</a>    <time class="time-badge time-ago">
      Connected 4 days ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12001" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Nicolas Bernal" data-ember-action="" data-ember-action-12002="12002">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Nicolas Bernal
      </span>

    </button>

<div id="ember12500" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12003" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12004" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Nicolas Bernal"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12005" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12006" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12007="12007">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Nicolas Bernal from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12008" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12010" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/deepak-chauhan-aa98758b/" id="ember12011" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12012" class="presence-entity presence-entity--size-5 ember-view"><img alt="Deepak Chauhan" id="ember12013" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5103AQHqeZSSu1sZ_A/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=PPb0EwleRWGHmw03sQ2kXFaedgEYFzHLN8WcPac3GrM">

<div id="ember12014" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/deepak-chauhan-aa98758b/" id="ember12015" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Deepak Chauhan
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Sr Art Director CGI at Target
    </span>
</a>    <time class="time-badge time-ago">
      Connected 4 days ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12016" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Deepak Chauhan" data-ember-action="" data-ember-action-12017="12017">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Deepak Chauhan
      </span>

    </button>

<div id="ember12490" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12018" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12019" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Deepak Chauhan"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12020" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12021" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12022="12022">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Deepak Chauhan from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12023" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12025" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/jasonoranzo/" id="ember12026" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12027" class="presence-entity presence-entity--size-5 ember-view"><img alt="Jason Oranzo" id="ember12028" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4E03AQGZfqyFiZAp3w/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=nuWnxPAesK-Tisg_KqFtna0aP7WHdKDhfFYNw_AGcL8">

<div id="ember12029" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/jasonoranzo/" id="ember12030" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Jason Oranzo
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Creative Director
    </span>
</a>    <time class="time-badge time-ago">
      Connected 4 days ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12031" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Jason Oranzo" data-ember-action="" data-ember-action-12032="12032">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Jason Oranzo
      </span>

    </button>

<div id="ember12501" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12033" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12034" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Jason Oranzo"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12035" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12036" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12037="12037">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Jason Oranzo from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12038" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12040" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/hannahtashkovich/" id="ember12041" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12042" class="presence-entity presence-entity--size-5 ember-view"><img alt="Hannah Tashkovich" id="ember12043" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5603AQGhoTHVF-TRQg/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=n0_U6EX8tR6l_L5mUcxg_SjYSSQ-_6EuqdgDHgaDvDo">

<div id="ember12044" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/hannahtashkovich/" id="ember12045" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Hannah Tashkovich
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Photo Editor/Photographer 
    </span>
</a>    <time class="time-badge time-ago">
      Connected 5 days ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12046" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Hannah Tashkovich" data-ember-action="" data-ember-action-12047="12047">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Hannah Tashkovich
      </span>

    </button>

<div id="ember12502" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12048" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12049" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Hannah Tashkovich"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12050" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12051" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12052="12052">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Hannah Tashkovich from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12053" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12055" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/johanna-fronek-36b39b13/" id="ember12056" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12057" class="presence-entity presence-entity--size-5 ember-view"><img alt="Johanna Fronek" id="ember12058" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4D03AQHL1kbLamulZg/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=akQiAtnQ2-Naz03BHXDMu4ufB2QQm5j1CG07uE3gDKg">

<div id="ember12059" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/johanna-fronek-36b39b13/" id="ember12060" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Johanna Fronek
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Director of Marketing - Creative Services at ONE Jeanswear Group
    </span>
</a>    <time class="time-badge time-ago">
      Connected 5 days ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12061" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Johanna Fronek" data-ember-action="" data-ember-action-12062="12062">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Johanna Fronek
      </span>

    </button>

<div id="ember12491" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12063" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12064" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Johanna Fronek"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12065" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12066" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12067="12067">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Johanna Fronek from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12068" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12070" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/alex-johnson-bb6692152/" id="ember12071" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12072" class="presence-entity presence-entity--size-5 ember-view"><img alt="Alex Johnson" id="ember12073" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4D03AQEvj4MSJHSKJw/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=7PK-qtLCvqNqJNY3kV4HvvphDjjSoa54WdG13xsLsG4">

<div id="ember12074" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/alex-johnson-bb6692152/" id="ember12075" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Alex Johnson
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Oppurtunist &amp; Image maker | 
Editor @ COPY London | Studio Manager @ Anomalous 
    </span>
</a>    <time class="time-badge time-ago">
      Connected 5 days ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12076" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Alex Johnson" data-ember-action="" data-ember-action-12077="12077">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Alex Johnson
      </span>

    </button>

<div id="ember12503" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12078" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12079" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Alex Johnson"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12080" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12081" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12082="12082">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Alex Johnson from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12083" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12085" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/stephanie-ponder-b674a51/" id="ember12086" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12087" class="presence-entity presence-entity--size-5 ember-view"><img alt="Stephanie Ponder" id="ember12088" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5103AQE_JoHuxxxbjg/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=N2GteLbvLyVGSAy735F8JTq6kGiM4DAKb_MaWQW38oE">

<div id="ember12089" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/stephanie-ponder-b674a51/" id="ember12090" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Stephanie Ponder
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Senior Editor at Costco Wholesale
    </span>
</a>    <time class="time-badge time-ago">
      Connected 5 days ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12091" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Stephanie Ponder" data-ember-action="" data-ember-action-12092="12092">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Stephanie Ponder
      </span>

    </button>

<div id="ember12504" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12093" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12094" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Stephanie Ponder"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12095" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12096" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12097="12097">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Stephanie Ponder from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12098" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12100" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/kyler-dannels-5a91798/" id="ember12101" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12102" class="presence-entity presence-entity--size-5 ember-view"><img alt="Kyler Dannels" id="ember12103" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5603AQHHmSwj7vzJzw/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=r7-P64MkovboeQPlVD2hpNmyfya84oKwQETy_an88wY">

<div id="ember12104" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/kyler-dannels-5a91798/" id="ember12105" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Kyler Dannels
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Art Department Creative Services
    </span>
</a>    <time class="time-badge time-ago">
      Connected 6 days ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12106" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Kyler Dannels" data-ember-action="" data-ember-action-12107="12107">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Kyler Dannels
      </span>

    </button>

<div id="ember12506" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12108" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12109" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Kyler Dannels"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12110" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12111" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12112="12112">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Kyler Dannels from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12113" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12115" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/sarineberberian/" id="ember12116" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12117" class="presence-entity presence-entity--size-5 ember-view"><img alt="Sarine Marie Berberian" id="ember12118" class=" presence-entity__image EntityPhoto-circle-5 lazy-image ember-view">

<div id="ember12119" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/sarineberberian/" id="ember12120" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Sarine Marie Berberian
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Studio Services Manager at Bloomingdale's
    </span>
</a>    <time class="time-badge time-ago">
      Connected 6 days ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12121" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Sarine Marie Berberian" data-ember-action="" data-ember-action-12122="12122">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Sarine Marie Berberian
      </span>

    </button>

<div id="ember12505" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12123" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12124" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Sarine Marie Berberian"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12125" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12126" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12127="12127">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Sarine Marie Berberian from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12128" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12130" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/tim-hollatz-65b32a4/" id="ember12131" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12132" class="presence-entity presence-entity--size-5 ember-view"><img alt="Tim Hollatz" id="ember12133" class=" presence-entity__image EntityPhoto-circle-5 lazy-image ember-view">

<div id="ember12134" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/tim-hollatz-65b32a4/" id="ember12135" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Tim Hollatz
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Senior Photographer at Target Corporation, Target Studio
    </span>
</a>    <time class="time-badge time-ago">
      Connected 6 days ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12136" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Tim Hollatz" data-ember-action="" data-ember-action-12137="12137">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Tim Hollatz
      </span>

    </button>

<div id="ember12507" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12138" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12139" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Tim Hollatz"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12140" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12141" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12142="12142">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Tim Hollatz from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12143" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12145" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/trevorpaulhus/" id="ember12146" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12147" class="presence-entity presence-entity--size-5 ember-view"><img alt="Trevor Paulhus" id="ember12148" class=" presence-entity__image EntityPhoto-circle-5 lazy-image ember-view">

<div id="ember12149" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/trevorpaulhus/" id="ember12150" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Trevor Paulhus
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Commercial / Editorial Photographer
    </span>
</a>    <time class="time-badge time-ago">
      Connected 6 days ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12151" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Trevor Paulhus" data-ember-action="" data-ember-action-12152="12152">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Trevor Paulhus
      </span>

    </button>

<div id="ember12508" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12153" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12154" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Trevor Paulhus"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12155" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12156" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12157="12157">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Trevor Paulhus from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12158" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12160" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/mattlangevin/" id="ember12161" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12162" class="presence-entity presence-entity--size-5 ember-view"><img alt="Matt Langevin" id="ember12163" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4D03AQHGiWR66ofD2w/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=zeAjpfdj8hx1s7LhvN_akxyzwL-A0QOnjK0MsY57Zs8">

<div id="ember12164" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/mattlangevin/" id="ember12165" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Matt Langevin
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Art Director &amp; Designer
    </span>
</a>    <time class="time-badge time-ago">
      Connected 6 days ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12166" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Matt Langevin" data-ember-action="" data-ember-action-12167="12167">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Matt Langevin
      </span>

    </button>

<div id="ember12509" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12168" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12169" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Matt Langevin"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12170" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12171" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12172="12172">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Matt Langevin from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12173" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12175" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/sidneybandynyc/" id="ember12176" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12177" class="presence-entity presence-entity--size-5 ember-view"><img alt="Sidney Bandy" id="ember12178" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4E03AQExCQ12fvN9yg/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=fpSxfUxxRKHjRi_O9u_Ty09KlqArFUxtnf9mKYQrjzc">

<div id="ember12179" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/sidneybandynyc/" id="ember12180" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Sidney Bandy
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Senior Mens Designer  at Johnston &amp; Murphy
    </span>
</a>    <time class="time-badge time-ago">
      Connected 6 days ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12181" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Sidney Bandy" data-ember-action="" data-ember-action-12182="12182">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Sidney Bandy
      </span>

    </button>

<div id="ember12510" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12183" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12184" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Sidney Bandy"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12185" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12186" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12187="12187">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Sidney Bandy from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12188" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12190" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/elijah--reaves/" id="ember12191" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12192" class="presence-entity presence-entity--size-5 ember-view"><img alt="Elijah Reaves" id="ember12193" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4E03AQHsvdXri2_IqA/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=9K7D5Pv4bDoquLoASOcJFm_o7OzV6HhZ_rHLgsUNodw">

<div id="ember12194" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/elijah--reaves/" id="ember12195" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Elijah Reaves
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      E-Commerce Photo Production Assistant at The RealReal
    </span>
</a>    <time class="time-badge time-ago">
      Connected 6 days ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12196" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Elijah Reaves" data-ember-action="" data-ember-action-12197="12197">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Elijah Reaves
      </span>

    </button>

<div id="ember12511" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12198" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12199" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Elijah Reaves"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12200" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12201" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12202="12202">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Elijah Reaves from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12203" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12205" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/leahpark/" id="ember12206" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12207" class="presence-entity presence-entity--size-5 ember-view"><img alt="Leah Park" id="ember12208" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4E03AQGl_8wZYdWa-A/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=L-lqobN7JNCkFxHc332mhigcwSJkV9JqGT_vPmt29fU">

<div id="ember12209" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/leahpark/" id="ember12210" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Leah Park
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Chief Creative Officer
    </span>
</a>    <time class="time-badge time-ago">
      Connected 6 days ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12211" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Leah Park" data-ember-action="" data-ember-action-12212="12212">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Leah Park
      </span>

    </button>

<div id="ember12492" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12213" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12214" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Leah Park"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12215" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12216" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12217="12217">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Leah Park from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12218" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12220" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/lupe-garcia-santiago-56ba6224/" id="ember12221" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12222" class="presence-entity presence-entity--size-5 ember-view"><img alt="Lupe Garcia Santiago" id="ember12223" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5603AQGuWWDpdNZATA/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=OIbM7z5SrH2Kf6NF1toDZ0-9ctAklNS_JC6Y85p76WY">

<div id="ember12224" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/lupe-garcia-santiago-56ba6224/" id="ember12225" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Lupe Garcia Santiago
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Studio Operations &amp; Production
    </span>
</a>    <time class="time-badge time-ago">
      Connected 6 days ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12226" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Lupe Garcia Santiago" data-ember-action="" data-ember-action-12227="12227">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Lupe Garcia Santiago
      </span>

    </button>

<div id="ember12493" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12228" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12229" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Lupe Garcia Santiago"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12230" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12231" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12232="12232">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Lupe Garcia Santiago from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12233" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12235" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/kiki-bowman/" id="ember12236" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12237" class="presence-entity presence-entity--size-5 ember-view"><img alt="Kiki Bowman" id="ember12238" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4D03AQHzNqq8SQ58bg/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=VzrJ5dBBcPQ69xtpi7_D_RNquDev_SuKFKojy3LtDy4">

<div id="ember12239" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/kiki-bowman/" id="ember12240" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Kiki Bowman
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Creative Operations Director at Wieden + Kennedy Tokyo
    </span>
</a>    <time class="time-badge time-ago">
      Connected 6 days ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12241" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Kiki Bowman" data-ember-action="" data-ember-action-12242="12242">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Kiki Bowman
      </span>

    </button>

<div id="ember12512" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12243" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12244" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Kiki Bowman"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12245" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12246" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12247="12247">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Kiki Bowman from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12248" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12250" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/megan-lee-4194b2144/" id="ember12251" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12252" class="presence-entity presence-entity--size-5 ember-view"><img alt="Megan Lee" id="ember12253" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5603AQEOgN2CklaKCw/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=310joioNttgMntN4PiBMhfyDFH1x8QVI3SJ7Fkej9aY">

<div id="ember12254" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/megan-lee-4194b2144/" id="ember12255" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Megan Lee
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Fashion Specialist at Amazon
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12256" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Megan Lee" data-ember-action="" data-ember-action-12257="12257">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Megan Lee
      </span>

    </button>

<div id="ember12513" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12258" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12259" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Megan Lee"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12260" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12261" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12262="12262">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Megan Lee from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12263" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12265" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/adamqueenimages/" id="ember12266" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12267" class="presence-entity presence-entity--size-5 ember-view"><img alt="Adam Queen" id="ember12268" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5603AQEtjGfXlfxQzA/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=PxffqFPf34hGBt_B4mmGAV26t8Y7IeMcE-bP64ljsso">

<div id="ember12269" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/adamqueenimages/" id="ember12270" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Adam Queen
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Director of Content Production at CreativeDrive
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12271" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Adam Queen" data-ember-action="" data-ember-action-12272="12272">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Adam Queen
      </span>

    </button>

<div id="ember12514" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12273" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12274" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Adam Queen"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12275" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12276" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12277="12277">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Adam Queen from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12278" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12280" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/andrea-hyde-2b35081/" id="ember12281" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12282" class="presence-entity presence-entity--size-5 ember-view"><img alt="Andrea Hyde" id="ember12283" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4E03AQGT-zh1gS5wNg/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=XKRZq-DD_cxE6MscfHBlNqaZeGpsjGMycBCGNyBjn3c">

<div id="ember12284" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/andrea-hyde-2b35081/" id="ember12285" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Andrea Hyde
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Creative Director
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12286" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Andrea Hyde" data-ember-action="" data-ember-action-12287="12287">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Andrea Hyde
      </span>

    </button>

<div id="ember12515" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12288" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12289" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Andrea Hyde"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12290" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12291" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12292="12292">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Andrea Hyde from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12293" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12295" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/joshgrant/" id="ember12296" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12297" class="presence-entity presence-entity--size-5 ember-view"><img alt="Josh Grant" id="ember12298" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5603AQGfRxXNjE9UWw/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=AFvXp9xLoAoo9WsGbvPbSV3LKzARYR1hD8EV8D4xDW4">

<div id="ember12299" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/joshgrant/" id="ember12300" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Josh Grant
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Producer at Zeus Jones Ltd.
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12301" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Josh Grant" data-ember-action="" data-ember-action-12302="12302">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Josh Grant
      </span>

    </button>

<div id="ember12516" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12303" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12304" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Josh Grant"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12305" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12306" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12307="12307">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Josh Grant from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12308" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12310" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/scott-gilson-63609647/" id="ember12311" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12312" class="presence-entity presence-entity--size-5 ember-view"><img alt="Scott Gilson" id="ember12313" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4E03AQGhrjxHeNErMA/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=RPylov_ovWB_QE96NUn2I2hTw04L5r8uBPRdN8iBnTE">

<div id="ember12314" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/scott-gilson-63609647/" id="ember12315" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Scott Gilson
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Creative Design Director at Wells Fargo
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12316" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Scott Gilson" data-ember-action="" data-ember-action-12317="12317">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Scott Gilson
      </span>

    </button>

<div id="ember12517" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12318" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12319" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Scott Gilson"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12320" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12321" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12322="12322">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Scott Gilson from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12323" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12325" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/julianvargasr/" id="ember12326" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12327" class="presence-entity presence-entity--size-5 ember-view"><img alt="Julian Vargas" id="ember12328" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4D03AQFQDwmozryBxQ/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=iS_hgf4fDVpUdIMprBem135CaL-VHe3vgXQgWYLWXXQ">

<div id="ember12329" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/julianvargasr/" id="ember12330" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Julian Vargas
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Senior Commercial Manager at BKR | Petroleum Engineer | Oil &amp; Gas Upstream Contracts Expert | MBA
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12331" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Julian Vargas" data-ember-action="" data-ember-action-12332="12332">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Julian Vargas
      </span>

    </button>

<div id="ember12518" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12333" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12334" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Julian Vargas"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12335" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12336" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12337="12337">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Julian Vargas from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12338" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12340" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/wade-shapley/" id="ember12341" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12342" class="presence-entity presence-entity--size-5 ember-view"><img alt="Wade Shapley" id="ember12343" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5603AQH9z-urA3QRWg/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=S1WJWnnARinCYZ_NcpKJzyBN1hgY3o3nXhegO05cIFk">

<div id="ember12344" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/wade-shapley/" id="ember12345" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Wade Shapley
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Creative Director/Head Designer (Owner W/S Designs) 
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12346" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Wade Shapley" data-ember-action="" data-ember-action-12347="12347">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Wade Shapley
      </span>

    </button>

<div id="ember12520" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12348" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12349" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Wade Shapley"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12350" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12351" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12352="12352">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Wade Shapley from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12353" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12355" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/kristopherlee/" id="ember12356" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12357" class="presence-entity presence-entity--size-5 ember-view"><img alt="Kristopher Lee" id="ember12358" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4E03AQEDJaRFRBUgkg/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=-3n9nbNLH-RWAj4u7U-DjIZN_QvIsNicC5oCgQ9me6E">

<div id="ember12359" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/kristopherlee/" id="ember12360" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Kristopher Lee
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Creative director, digital marketing and advertising
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12361" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Kristopher Lee" data-ember-action="" data-ember-action-12362="12362">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Kristopher Lee
      </span>

    </button>

<div id="ember12519" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12363" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12364" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Kristopher Lee"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12365" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12366" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12367="12367">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Kristopher Lee from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12368" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12370" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/stephenctwong/" id="ember12371" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12372" class="presence-entity presence-entity--size-5 ember-view"><img alt="Stephen Wong" id="ember12373" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5603AQFBCvHQcuAc0g/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=ePGW26k3eP6Jkqls64fWpXbIDJ-7oUYw0WZs683k3gg">

<div id="ember12374" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/stephenctwong/" id="ember12375" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Stephen Wong
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Creative Director
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12376" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Stephen Wong" data-ember-action="" data-ember-action-12377="12377">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Stephen Wong
      </span>

    </button>

<div id="ember12525" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12378" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12379" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Stephen Wong"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12380" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12381" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12382="12382">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Stephen Wong from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12383" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12385" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/danicaobrien/" id="ember12386" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12387" class="presence-entity presence-entity--size-5 ember-view"><img alt="Danica O&amp;#39;Brien" id="ember12388" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5603AQFyf2kzzEyCVg/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=XjQdmfIyndlo3bpqoZRmHupNh0Tcd468uhPmOqbempE">

<div id="ember12389" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/danicaobrien/" id="ember12390" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Danica O'Brien
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      VP, Creative Services
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12391" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Danica O&amp;#39;Brien" data-ember-action="" data-ember-action-12392="12392">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Danica O'Brien
      </span>

    </button>

<div id="ember12521" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12393" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12394" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Danica O&amp;#39;Brien"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12395" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12396" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12397="12397">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Danica O&amp;#39;Brien from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12398" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12400" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/michaeljasonenriquez/" id="ember12401" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12402" class="presence-entity presence-entity--size-5 ember-view"><img alt="Michael Jason Enriquez" id="ember12403" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5603AQH1oKwrHGuyXw/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=hLUWLSLw2zCxPQZ3P1gUZibD5aQhnmy74pzeREYZHo0">

<div id="ember12404" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/michaeljasonenriquez/" id="ember12405" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Michael Jason Enriquez
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Senior Creative at Credit Karma
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12406" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Michael Jason Enriquez" data-ember-action="" data-ember-action-12407="12407">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Michael Jason Enriquez
      </span>

    </button>

<div id="ember12523" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12408" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12409" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Michael Jason Enriquez"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12410" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12411" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12412="12412">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Michael Jason Enriquez from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12413" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12415" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/shabria-major-22388b86/" id="ember12416" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12417" class="presence-entity presence-entity--size-5 ember-view"><img alt="Shabria Major" id="ember12418" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5603AQF-PckjQeP49g/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=SnqS3R-2yg2ozfvy2IIeOeux2j6qFUuA9p1jTdQKJuk">

<div id="ember12419" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/shabria-major-22388b86/" id="ember12420" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Shabria Major
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Stylist Freelancer
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12421" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Shabria Major" data-ember-action="" data-ember-action-12422="12422">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Shabria Major
      </span>

    </button>

<div id="ember12522" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12423" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12424" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Shabria Major"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12425" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12426" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12427="12427">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Shabria Major from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12428" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12430" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/margaretlambert/" id="ember12431" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12432" class="presence-entity presence-entity--size-5 ember-view"><img alt="Margaret Lambert" id="ember12433" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4D03AQGcAuQWCyyjDA/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=01CxDh0P7w2V56HnR20T-mBZhW_a_84n6XdYw3vjsBY">

<div id="ember12434" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/margaretlambert/" id="ember12435" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Margaret Lambert
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Director, Digital &amp; Creative Division at Green Key Resources
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12436" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Margaret Lambert" data-ember-action="" data-ember-action-12437="12437">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Margaret Lambert
      </span>

    </button>

<div id="ember12524" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12438" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12439" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Margaret Lambert"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12440" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12441" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12442="12442">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Margaret Lambert from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12443" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12445" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/petegiblin/" id="ember12446" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12447" class="presence-entity presence-entity--size-5 ember-view"><img alt="Pete Giblin" id="ember12448" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4E03AQE1BEAIAMwd8g/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=ziYQhoPwu2M1hPBhngemcWipTnRFvp2TolDIDQtgYT0">

<div id="ember12449" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/petegiblin/" id="ember12450" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Pete Giblin
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Director / Creative
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12451" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Pete Giblin" data-ember-action="" data-ember-action-12452="12452">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Pete Giblin
      </span>

    </button>

<div id="ember12526" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12453" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12454" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Pete Giblin"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12455" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12456" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12457="12457">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Pete Giblin from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12458" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12460" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/craig-paull/" id="ember12461" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12462" class="presence-entity presence-entity--size-5 ember-view"><img alt="Craig Paull" id="ember12463" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4E03AQFLOaupsb80Jw/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=dAafqVDVg1dfYgmIiN0M1gKgnaAOI1Nj7hHJkG-vaZM">

<div id="ember12464" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/craig-paull/" id="ember12465" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Craig Paull
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Director - Image Lab at Bed Bath &amp; Beyond
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12466" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Craig Paull" data-ember-action="" data-ember-action-12467="12467">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Craig Paull
      </span>

    </button>

<div id="ember12527" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12468" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12469" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Craig Paull"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12470" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12471" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12472="12472">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Craig Paull from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12473" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12475" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/ayubuazizi/" id="ember12476" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12477" class="presence-entity presence-entity--size-5 ember-view"><img alt="Ayubu Azizi" id="ember12478" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5603AQFKPkqZqtT7Cw/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=diPKgOi77sgqN8Ahc6YJoRJUrykM9i-u2xXq2bDCrs4">

<div id="ember12479" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/ayubuazizi/" id="ember12480" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Ayubu Azizi
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Associate Creative Director at The Sandbox Agency
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12481" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Ayubu Azizi" data-ember-action="" data-ember-action-12482="12482">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Ayubu Azizi
      </span>

    </button>

<div id="ember12528" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12483" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12484" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Ayubu Azizi"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12485" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12486" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12487="12487">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Ayubu Azizi from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12488" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12531" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/chris-skiles-6479a88/" id="ember12532" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12533" class="presence-entity presence-entity--size-5 ember-view"><img alt="Chris Skiles" id="ember12534" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4D03AQFkutXNdDT-nA/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=WcE-grEFzM6HvwoO2vZsRzqcT04JkNvdwmID_N_oF6c">

<div id="ember12535" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/chris-skiles-6479a88/" id="ember12536" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Chris Skiles
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Associate Creative Director at Crocs
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12537" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Chris Skiles" data-ember-action="" data-ember-action-12538="12538">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Chris Skiles
      </span>

    </button>

<div id="ember13135" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12539" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12540" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Chris Skiles"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12541" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12542" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12543="12543">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Chris Skiles from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12544" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12546" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/aaronbelford/" id="ember12547" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12548" class="presence-entity presence-entity--size-5 ember-view"><img alt="Aaron Belford" id="ember12549" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4E03AQFnpHGpwAGdXQ/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=lX7K8bA0ttiM2YUpGwn131AhdiP3Tvyqxs879Xc5gek">

<div id="ember12550" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/aaronbelford/" id="ember12551" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Aaron Belford
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Creative Director at BIKEMAN PERFORMANCE
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12552" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Aaron Belford" data-ember-action="" data-ember-action-12553="12553">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Aaron Belford
      </span>

    </button>

<div id="ember13136" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12554" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12555" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Aaron Belford"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12556" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12557" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12558="12558">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Aaron Belford from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12559" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12561" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/mitchell-murphy-2b862a/" id="ember12562" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12563" class="presence-entity presence-entity--size-5 ember-view"><img alt="Mitchell Murphy" id="ember12564" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4E03AQFYPEdwJ21C7w/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=sgeWu0oFG9JNvXZRRBzmvrBvdFKuaGyumcJHewPn2EQ">

<div id="ember12565" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/mitchell-murphy-2b862a/" id="ember12566" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Mitchell Murphy
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Make good.
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12567" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Mitchell Murphy" data-ember-action="" data-ember-action-12568="12568">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Mitchell Murphy
      </span>

    </button>

<div id="ember13137" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12569" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12570" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Mitchell Murphy"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12571" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12572" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12573="12573">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Mitchell Murphy from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12574" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12576" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/glosinda-goes-53643a53/" id="ember12577" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12578" class="presence-entity presence-entity--size-5 ember-view"><img alt="Glosinda Goes" id="ember12579" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5103AQGtI0XSIqMABA/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=dqhHPifk9hUjFpD150V-f2fL6zMLbkc7nHE-LSvA-tY">

<div id="ember12580" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/glosinda-goes-53643a53/" id="ember12581" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Glosinda Goes
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Global Partnerships and Affiliates Manager at Crabtree and Evelyn 
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12582" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Glosinda Goes" data-ember-action="" data-ember-action-12583="12583">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Glosinda Goes
      </span>

    </button>

<div id="ember13138" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12584" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12585" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Glosinda Goes"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12586" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12587" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12588="12588">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Glosinda Goes from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12589" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12591" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/nairinajarian/" id="ember12592" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12593" class="presence-entity presence-entity--size-5 ember-view"><img alt="Nairi Najarian" id="ember12594" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5603AQFAw6qhggnsVQ/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=fD-GH1w-j9hzpla7bDe3xQwiwQHWmqKUJi-ogqCTPbE">

<div id="ember12595" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/nairinajarian/" id="ember12596" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Nairi Najarian
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Sr. Director, Digital Marketing at Create &amp; Cultivate
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12597" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Nairi Najarian" data-ember-action="" data-ember-action-12598="12598">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Nairi Najarian
      </span>

    </button>

<div id="ember13139" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12599" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12600" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Nairi Najarian"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12601" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12602" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12603="12603">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Nairi Najarian from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12604" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12606" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/kareemquowphotography/" id="ember12607" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12608" class="presence-entity presence-entity--size-5 ember-view"><img alt="Kareem Quow" id="ember12609" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5603AQH7w2K9FLgqnQ/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=wWiETpbOi5t_X9Uu_xVy64qxp9lbZyU5LxvM4wDg6Tw">

<div id="ember12610" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/kareemquowphotography/" id="ember12611" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Kareem Quow
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Beauty + Fashion + Conceptual  Photographer
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12612" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Kareem Quow" data-ember-action="" data-ember-action-12613="12613">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Kareem Quow
      </span>

    </button>

<div id="ember13140" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12614" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12615" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Kareem Quow"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12616" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12617" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12618="12618">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Kareem Quow from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12619" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12621" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/katieroletto/" id="ember12622" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12623" class="presence-entity presence-entity--size-5 ember-view"><img alt="Katie Roletto Faulknor" id="ember12624" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5603AQFwxhZ5cjLBBg/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=gowJHiYKtrFPDge0At8cNt2ZfjGMZT4HatDD861pdA4">

<div id="ember12625" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/katieroletto/" id="ember12626" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Katie Roletto Faulknor
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Lead Video Producer at Benefit Cosmetics
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12627" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Katie Roletto Faulknor" data-ember-action="" data-ember-action-12628="12628">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Katie Roletto Faulknor
      </span>

    </button>

<div id="ember13130" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12629" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12630" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Katie Roletto Faulknor"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12631" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12632" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12633="12633">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Katie Roletto Faulknor from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12634" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12636" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/tanicoutts/" id="ember12637" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12638" class="presence-entity presence-entity--size-5 ember-view"><img alt="Ara Tani Coutts" id="ember12639" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4E03AQGsraIJBtq5pw/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=aMD-TnKTXKfsWddLJWpVIZzPluQ2JjmPCoWWzeKO3OA">

<div id="ember12640" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/tanicoutts/" id="ember12641" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Ara Tani Coutts
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      enterprise cloud solutions, ecom, visual artist
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12642" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Ara Tani Coutts" data-ember-action="" data-ember-action-12643="12643">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Ara Tani Coutts
      </span>

    </button>

<div id="ember13141" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12644" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12645" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Ara Tani Coutts"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12646" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12647" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12648="12648">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Ara Tani Coutts from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12649" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12651" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/betsy-mullinix-97096319/" id="ember12652" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12653" class="presence-entity presence-entity--size-5 ember-view"><img alt="Betsy Mullinix" id="ember12654" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4D03AQE-cxjkv9gU-Q/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=_ZzQQdi4_NRDVd6REyGNrEkKYJizLrGd6hPK2a04A20">

<div id="ember12655" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/betsy-mullinix-97096319/" id="ember12656" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Betsy Mullinix
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Art Director at Amazon
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12657" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Betsy Mullinix" data-ember-action="" data-ember-action-12658="12658">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Betsy Mullinix
      </span>

    </button>

<div id="ember13142" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12659" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12660" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Betsy Mullinix"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12661" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12662" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12663="12663">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Betsy Mullinix from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12664" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12666" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/priscatozzi/" id="ember12667" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12668" class="presence-entity presence-entity--size-5 ember-view"><img alt="Prisca Tozzi" id="ember12669" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4D03AQGGlI9PK-0tFg/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=KbM2D2BgyGUkf8Y7A3hZmlXsB2fv6NG9TEOudBIKoN4">

<div id="ember12670" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/priscatozzi/" id="ember12671" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Prisca Tozzi
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Freelance Photographer presso ASOS
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12672" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Prisca Tozzi" data-ember-action="" data-ember-action-12673="12673">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Prisca Tozzi
      </span>

    </button>

<div id="ember13131" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12674" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12675" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Prisca Tozzi"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12676" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12677" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12678="12678">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Prisca Tozzi from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12679" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12681" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/michael-seitz-191aa213/" id="ember12682" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12683" class="presence-entity presence-entity--size-5 ember-view"><img alt="Michael Seitz" id="ember12684" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4D03AQEq4P8TvdJLPg/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=RVg5We5cOjeEi4-XqOcN6FdpCc_u8qknf8Sh96g8DGA">

<div id="ember12685" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/michael-seitz-191aa213/" id="ember12686" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Michael Seitz
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Associate Creative Director at Fellow
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12687" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Michael Seitz" data-ember-action="" data-ember-action-12688="12688">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Michael Seitz
      </span>

    </button>

<div id="ember13132" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12689" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12690" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Michael Seitz"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12691" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12692" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12693="12693">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Michael Seitz from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12694" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12696" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/susanesheffield/" id="ember12697" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12698" class="presence-entity presence-entity--size-5 ember-view"><img alt="Susan Sheffield" id="ember12699" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4D03AQEV5aEHIkAvBg/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=Y0Tu0xwcRQp9KhiDAgfplAJoFJHAjNJ5xBAJSzi5Tdw">

<div id="ember12700" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/susanesheffield/" id="ember12701" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Susan Sheffield
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Design Director for Art &amp; Textiles at Target
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12702" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Susan Sheffield" data-ember-action="" data-ember-action-12703="12703">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Susan Sheffield
      </span>

    </button>

<div id="ember13143" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12704" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12705" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Susan Sheffield"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12706" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12707" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12708="12708">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Susan Sheffield from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12709" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12711" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/jeremy-postell-66167830/" id="ember12712" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12713" class="presence-entity presence-entity--size-5 ember-view"><img alt="Jeremy Postell" id="ember12714" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5603AQGQvHTA_X6RVA/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=ZQRsYmLGr-IYx7_US8tVMALNlXyEpsGxe0T9KYlA91s">

<div id="ember12715" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/jeremy-postell-66167830/" id="ember12716" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Jeremy Postell
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      let's create, let's think, let's figure it out.

    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12717" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Jeremy Postell" data-ember-action="" data-ember-action-12718="12718">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Jeremy Postell
      </span>

    </button>

<div id="ember13144" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12719" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12720" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Jeremy Postell"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12721" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12722" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12723="12723">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Jeremy Postell from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12724" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12726" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/mitchell-severs/" id="ember12727" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12728" class="presence-entity presence-entity--size-5 ember-view"><img alt="Mitchell Severs" id="ember12729" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4D03AQEKA_DanL2cLQ/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=ynLlosAyMX-WGoIMwVzzkD5sDJWXXlQxgZvXj65PgQw">

<div id="ember12730" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/mitchell-severs/" id="ember12731" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Mitchell Severs
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Fashion Photographer, Creative Director and Retoucher
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12732" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Mitchell Severs" data-ember-action="" data-ember-action-12733="12733">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Mitchell Severs
      </span>

    </button>

<div id="ember13146" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12734" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12735" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Mitchell Severs"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12736" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12737" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12738="12738">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Mitchell Severs from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12739" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12741" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/letter2self/" id="ember12742" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12743" class="presence-entity presence-entity--size-5 ember-view"><img alt="Danie Williams-Rivera" id="ember12744" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4E03AQHMs_WwYt7G_w/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=iMyzgPWQGr43wdDJlmvi4-KK1evKzgrCGLOU1pO_2Bc">

<div id="ember12745" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/letter2self/" id="ember12746" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Danie Williams-Rivera
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Digital Marketing Manager at Lands'&#8203; End
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12747" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Danie Williams-Rivera" data-ember-action="" data-ember-action-12748="12748">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Danie Williams-Rivera
      </span>

    </button>

<div id="ember13145" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12749" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12750" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Danie Williams-Rivera"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12751" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12752" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12753="12753">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Danie Williams-Rivera from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12754" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12756" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/arianna-oggioni-43920631/" id="ember12757" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12758" class="presence-entity presence-entity--size-5 ember-view"><img alt="Arianna Oggioni" id="ember12759" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5603AQF8b3BIk1490w/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=K-Eo7P3FDx_cdkIDKPaEQB9BInL8iXXMoNSlCwymWUc">

<div id="ember12760" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/arianna-oggioni-43920631/" id="ember12761" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Arianna Oggioni
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Post Production Manager presso Diesel
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12762" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Arianna Oggioni" data-ember-action="" data-ember-action-12763="12763">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Arianna Oggioni
      </span>

    </button>

<div id="ember13147" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12764" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12765" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Arianna Oggioni"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12766" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12767" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12768="12768">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Arianna Oggioni from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12769" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12771" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/nikimustain/" id="ember12772" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12773" class="presence-entity presence-entity--size-5 ember-view"><img alt="Niki Mustain" id="ember12774" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4E03AQG-LIvCyafxAg/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=llC842si7dJ_i0wPJNTag-fIZD2k3uszrwDMpatsmcM">

<div id="ember12775" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/nikimustain/" id="ember12776" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Niki Mustain
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Product Manager - Optics at The Tiffen Company
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12777" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Niki Mustain" data-ember-action="" data-ember-action-12778="12778">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Niki Mustain
      </span>

    </button>

<div id="ember13148" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12779" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12780" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Niki Mustain"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12781" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12782" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12783="12783">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Niki Mustain from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12784" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12786" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/hannah-massey-a5459067/" id="ember12787" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12788" class="presence-entity presence-entity--size-5 ember-view"><img alt="Hannah Massey" id="ember12789" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5603AQHVV_4DVSua6A/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=K24d5WMctTvr2pHB1fXYAD0o9Y-oImJJ2QPHXynYRm0">

<div id="ember12790" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/hannah-massey-a5459067/" id="ember12791" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Hannah Massey
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Photo Studio Manager at Primark
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12792" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Hannah Massey" data-ember-action="" data-ember-action-12793="12793">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Hannah Massey
      </span>

    </button>

<div id="ember13149" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12794" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12795" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Hannah Massey"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12796" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12797" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12798="12798">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Hannah Massey from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12799" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12801" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/gemma-di-giovanni-169b47134/" id="ember12802" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12803" class="presence-entity presence-entity--size-5 ember-view"><img alt="Gemma Di Giovanni" id="ember12804" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4D03AQEZMPUwrjujqA/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=aOxY8yMS_Q77ZbBM-c3oV6kpQgFZuMIw-f-lmYrCyNc">

<div id="ember12805" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/gemma-di-giovanni-169b47134/" id="ember12806" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Gemma Di Giovanni
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Illustrator/Creative Artworker at Clarks
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12807" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Gemma Di Giovanni" data-ember-action="" data-ember-action-12808="12808">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Gemma Di Giovanni
      </span>

    </button>

<div id="ember13152" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12809" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12810" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Gemma Di Giovanni"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12811" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12812" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12813="12813">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Gemma Di Giovanni from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12814" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12816" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/kahlil-reyes-a251284/" id="ember12817" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12818" class="presence-entity presence-entity--size-5 ember-view"><img alt="Kahlil Reyes" id="ember12819" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4E03AQHICAGZuXLDpw/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=Ha9VrYIOltlPob7s3vn9eAiaX_gLcodME_ZsnxyGEKs">

<div id="ember12820" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/kahlil-reyes-a251284/" id="ember12821" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Kahlil Reyes
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Executive | Luxury | Retail | Fitness
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12822" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Kahlil Reyes" data-ember-action="" data-ember-action-12823="12823">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Kahlil Reyes
      </span>

    </button>

<div id="ember13151" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12824" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12825" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Kahlil Reyes"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12826" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12827" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12828="12828">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Kahlil Reyes from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12829" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12831" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/ekincanbayrakdar/" id="ember12832" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12833" class="presence-entity presence-entity--size-5 ember-view"><img alt="Ekin Can Bayrakdar" id="ember12834" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4E03AQEpKsVd77G20g/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=RosJbBF7S2ZBx5tTo02ti3LGmsezgG-jGuVxvQiCA0k">

<div id="ember12835" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/ekincanbayrakdar/" id="ember12836" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Ekin Can Bayrakdar
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Fashion Photographer
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12837" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Ekin Can Bayrakdar" data-ember-action="" data-ember-action-12838="12838">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Ekin Can Bayrakdar
      </span>

    </button>

<div id="ember13150" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12839" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12840" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Ekin Can Bayrakdar"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12841" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12842" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12843="12843">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Ekin Can Bayrakdar from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12844" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12846" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/marta-krakowiecka-4987a983/" id="ember12847" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12848" class="presence-entity presence-entity--size-5 ember-view"><img alt="Marta Krakowiecka" id="ember12849" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4E03AQFHQtbiNcK_Yg/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=6LW6CAi2VcPLp1s09RouA8ahYPty-cqMurnosDdfHCY">

<div id="ember12850" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/marta-krakowiecka-4987a983/" id="ember12851" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Marta Krakowiecka
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Photographer ➱ 4x M Photography
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12852" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Marta Krakowiecka" data-ember-action="" data-ember-action-12853="12853">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Marta Krakowiecka
      </span>

    </button>

<div id="ember13153" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12854" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12855" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Marta Krakowiecka"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12856" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12857" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12858="12858">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Marta Krakowiecka from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12859" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12861" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/keenan-jones-4239681a/" id="ember12862" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12863" class="presence-entity presence-entity--size-5 ember-view"><img alt="Keenan Jones" id="ember12864" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5603AQGptS8BdWvKLQ/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=BgVHsL5zpx4vi2rPrS93ijBCrfyXprLhWvu78aabMpQ">

<div id="ember12865" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/keenan-jones-4239681a/" id="ember12866" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Keenan Jones
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Digital Collections Manager, Department of Nike Archives
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12867" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Keenan Jones" data-ember-action="" data-ember-action-12868="12868">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Keenan Jones
      </span>

    </button>

<div id="ember13154" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12869" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12870" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Keenan Jones"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12871" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12872" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12873="12873">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Keenan Jones from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12874" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12876" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/tania-ray-1b6931175/" id="ember12877" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12878" class="presence-entity presence-entity--size-5 ember-view"><img alt="Tania Ray" id="ember12879" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4D03AQHjtx6fUAImGA/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=BblGnWzyXDRiKFSEpZhFYNPQw8MTuha5vmWaWTm4aNI">

<div id="ember12880" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/tania-ray-1b6931175/" id="ember12881" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Tania Ray
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Freelance Photographer at Tania Ray Photography
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12882" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Tania Ray" data-ember-action="" data-ember-action-12883="12883">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Tania Ray
      </span>

    </button>

<div id="ember13155" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12884" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12885" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Tania Ray"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12886" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12887" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12888="12888">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Tania Ray from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12889" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12891" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/dariocastillostudio/" id="ember12892" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12893" class="presence-entity presence-entity--size-5 ember-view"><img alt="Dario Castillo" id="ember12894" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4E03AQEgfIYvVX1Ctw/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=HxlyhoYXoxVQN69XWSj3d4GpOcwWCkASSU8RasTGnrY">

<div id="ember12895" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/dariocastillostudio/" id="ember12896" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Dario Castillo
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Dario Castillo
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12897" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Dario Castillo" data-ember-action="" data-ember-action-12898="12898">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Dario Castillo
      </span>

    </button>

<div id="ember13156" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12899" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12900" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Dario Castillo"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12901" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12902" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12903="12903">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Dario Castillo from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12904" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12906" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/reemshuga/" id="ember12907" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12908" class="presence-entity presence-entity--size-5 ember-view"><img alt="Reem Shuga" id="ember12909" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4D03AQHQVzL0zsB1pw/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=qdO2uKfBnhK680xPVkWuUQbVt1Wmlc2a_iiaIzm2vf4">

<div id="ember12910" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/reemshuga/" id="ember12911" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Reem Shuga
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Studio Designer at Publix Super Markets
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12912" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Reem Shuga" data-ember-action="" data-ember-action-12913="12913">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Reem Shuga
      </span>

    </button>

<div id="ember13157" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12914" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12915" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Reem Shuga"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12916" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12917" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12918="12918">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Reem Shuga from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12919" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12921" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/yasminmajidi/" id="ember12922" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12923" class="presence-entity presence-entity--size-5 ember-view"><img alt="Yasmin Majidi" id="ember12924" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4E03AQFnIcu6TupGow/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=I05nD2cgECqPkaochxd4k2dsFKV0wvV8pNgxfEXMbJQ">

<div id="ember12925" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/yasminmajidi/" id="ember12926" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Yasmin Majidi
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Creative Director at YMYL New York 
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12927" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Yasmin Majidi" data-ember-action="" data-ember-action-12928="12928">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Yasmin Majidi
      </span>

    </button>

<div id="ember13158" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12929" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12930" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Yasmin Majidi"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12931" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12932" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12933="12933">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Yasmin Majidi from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12934" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12936" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/paulwl/" id="ember12937" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12938" class="presence-entity presence-entity--size-5 ember-view"><img alt="Paul Wilde L&amp;#39;Heureux" id="ember12939" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4D03AQG_nHi_FzMOdg/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=IEZiXd4S_3KMrwnssL25l-m2J8cbSW4OFlqCelCTRYo">

<div id="ember12940" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/paulwl/" id="ember12941" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Paul Wilde L'Heureux
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      We’re hiring! Check out open Target Creative roles at Target.com/careers. 
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12942" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Paul Wilde L&amp;#39;Heureux" data-ember-action="" data-ember-action-12943="12943">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Paul Wilde L'Heureux
      </span>

    </button>

<div id="ember13159" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12944" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12945" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Paul Wilde L&amp;#39;Heureux"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12946" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12947" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12948="12948">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Paul Wilde L&amp;#39;Heureux from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12949" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12951" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/inkstasy/" id="ember12952" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12953" class="presence-entity presence-entity--size-5 ember-view"><img alt="Kinjal Mitra" id="ember12954" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4E03AQGjRAcLz6GoNw/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=X0AKfe5LpZlH-lmVkzo-MKelFDwfo-N2mCIaIvneAHk">

<div id="ember12955" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/inkstasy/" id="ember12956" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Kinjal Mitra
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Freelance Retoucher 
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12957" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Kinjal Mitra" data-ember-action="" data-ember-action-12958="12958">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Kinjal Mitra
      </span>

    </button>

<div id="ember13161" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12959" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12960" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Kinjal Mitra"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12961" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12962" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12963="12963">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Kinjal Mitra from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12964" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12966" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/rccavin22/" id="ember12967" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12968" class="presence-entity presence-entity--size-5 ember-view"><img alt="Ryan Cavin" id="ember12969" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5603AQEJ9avfeNCAkg/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=HNmVX0DJ07F6HGsHaing5b8xwXGHL0NaJxoZmKgPX8A">

<div id="ember12970" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/rccavin22/" id="ember12971" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Ryan Cavin
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Stylist at Nike
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12972" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Ryan Cavin" data-ember-action="" data-ember-action-12973="12973">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Ryan Cavin
      </span>

    </button>

<div id="ember13160" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12974" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12975" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Ryan Cavin"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12976" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12977" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12978="12978">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Ryan Cavin from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12979" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12981" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/seattle-voice-talent/" id="ember12982" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12983" class="presence-entity presence-entity--size-5 ember-view"><img alt="Joshua Alexander Voiceover Artist" id="ember12984" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5603AQFxOpj9U1rMmg/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=sYPCfQ9MX97FDClACn2IbAuh_mkGNY5950_iknRCWxY">

<div id="ember12985" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/seattle-voice-talent/" id="ember12986" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Joshua Alexander Voiceover Artist
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      &lt;1 Hour turnaround Voiceover Artist for E-Learning, Explainer Videos, Commercial Narration Voice-over. No Hassle &amp; Affordable
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember12987" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Joshua Alexander Voiceover Artist" data-ember-action="" data-ember-action-12988="12988">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Joshua Alexander Voiceover Artist
      </span>

    </button>

<div id="ember13133" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember12989" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember12990" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Joshua Alexander Voiceover Artist"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember12991" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember12992" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-12993="12993">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Joshua Alexander Voiceover Artist from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember12994" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember12996" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/sherman-pereira-34109b193/" id="ember12997" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember12998" class="presence-entity presence-entity--size-5 ember-view"><img alt="Sherman Pereira" id="ember12999" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5603AQEC7UQCm29OHw/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=GrFwXy_dBcX1S-S8cckcK4b6nVi1EpV0qJn0_lnntek">

<div id="ember13000" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/sherman-pereira-34109b193/" id="ember13001" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Sherman Pereira
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      " I have a work Ethic. if i say i'm going to do something, I do it."
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember13002" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Sherman Pereira" data-ember-action="" data-ember-action-13003="13003">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Sherman Pereira
      </span>

    </button>

<div id="ember13162" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember13004" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember13005" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Sherman Pereira"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember13006" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember13007" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-13008="13008">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Sherman Pereira from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember13009" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember13011" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/jessica-grundle-b07a32170/" id="ember13012" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember13013" class="presence-entity presence-entity--size-5 ember-view"><img alt="Jessica Grundle" id="ember13014" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4E03AQEfMUVwaJPdHw/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=suqmJPFSAkT8kpWdDcuAayY6Y6DlrTDqeyGoWw9gaOY">

<div id="ember13015" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/jessica-grundle-b07a32170/" id="ember13016" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Jessica Grundle
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Junior Retoucher at JD Sports
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember13017" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Jessica Grundle" data-ember-action="" data-ember-action-13018="13018">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Jessica Grundle
      </span>

    </button>

<div id="ember13163" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember13019" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember13020" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Jessica Grundle"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember13021" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember13022" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-13023="13023">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Jessica Grundle from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember13024" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember13026" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/brian-high-010763189/" id="ember13027" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember13028" class="presence-entity presence-entity--size-5 ember-view"><img alt="Brian High" id="ember13029" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4E03AQFysrjg24ICxw/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=qusI3hyOgcZ-MdEOgX4YN2fbJ31BPJf0CglIHd9Tha8">

<div id="ember13030" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/brian-high-010763189/" id="ember13031" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Brian High
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Photographer/ Retoucher
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember13032" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Brian High" data-ember-action="" data-ember-action-13033="13033">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Brian High
      </span>

    </button>

<div id="ember13134" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember13034" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember13035" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Brian High"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember13036" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember13037" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-13038="13038">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Brian High from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember13039" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember13041" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/carolyn-reilley-95700819/" id="ember13042" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember13043" class="presence-entity presence-entity--size-5 ember-view"><img alt="Carolyn Reilley" id="ember13044" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4E03AQE0JRUfoa8AOg/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=usCFt-FN0QfUQMsn35CIrlITb6zhttRgySlXHzI7hAc">

<div id="ember13045" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/carolyn-reilley-95700819/" id="ember13046" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Carolyn Reilley
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Art Director
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember13047" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Carolyn Reilley" data-ember-action="" data-ember-action-13048="13048">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Carolyn Reilley
      </span>

    </button>

<div id="ember13164" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember13049" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember13050" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Carolyn Reilley"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember13051" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember13052" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-13053="13053">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Carolyn Reilley from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember13054" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember13056" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/kellydao/" id="ember13057" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember13058" class="presence-entity presence-entity--size-5 ember-view"><img alt="Kelly Dao" id="ember13059" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5603AQHoi-uCZ6njLQ/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=YxAr1sTQLAzkc0X2ar6DaA01e36XlHCfdvot9yUH_6o">

<div id="ember13060" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/kellydao/" id="ember13061" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Kelly Dao
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Candid™ Seattle Manager
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember13062" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Kelly Dao" data-ember-action="" data-ember-action-13063="13063">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Kelly Dao
      </span>

    </button>

<div id="ember13165" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember13064" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember13065" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Kelly Dao"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember13066" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember13067" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-13068="13068">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Kelly Dao from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember13069" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember13071" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/thompsonobrandon/" id="ember13072" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember13073" class="presence-entity presence-entity--size-5 ember-view"><img alt="Brandon O. Thompson" id="ember13074" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4E03AQHWwi-N1HQLvw/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=W4j5KMFoJ38Nu8yB_TQAjWFBESRYOy7W3U1nsiSeemc">

<div id="ember13075" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/thompsonobrandon/" id="ember13076" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Brandon O. Thompson
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Freelance Assistant + Marketing 
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember13077" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Brandon O. Thompson" data-ember-action="" data-ember-action-13078="13078">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Brandon O. Thompson
      </span>

    </button>

<div id="ember13166" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember13079" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember13080" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Brandon O. Thompson"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember13081" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember13082" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-13083="13083">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Brandon O. Thompson from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember13084" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember13086" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/brian-holt-4a82291/" id="ember13087" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember13088" class="presence-entity presence-entity--size-5 ember-view"><img alt="Brian Holt" id="ember13089" class=" presence-entity__image EntityPhoto-circle-5 lazy-image ghost-person loaded ember-view" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7">

<div id="ember13090" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/brian-holt-4a82291/" id="ember13091" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Brian Holt
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Senior Art Director/Graphic Designer at Target
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember13092" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Brian Holt" data-ember-action="" data-ember-action-13093="13093">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Brian Holt
      </span>

    </button>

<div id="ember13168" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember13094" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember13095" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Brian Holt"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember13096" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember13097" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-13098="13098">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Brian Holt from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember13099" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember13101" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/alyssa-dineen-515a0bb/" id="ember13102" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember13103" class="presence-entity presence-entity--size-5 ember-view"><img alt="Alyssa Dineen" id="ember13104" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5603AQE0_a-1gFdFgA/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=sAFgRKLcQcfVMjxQXBqEiV11EEBJ2z_Mc8K_PHosQBI">

<div id="ember13105" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/alyssa-dineen-515a0bb/" id="ember13106" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Alyssa Dineen
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Founder at Style My Profile
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember13107" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Alyssa Dineen" data-ember-action="" data-ember-action-13108="13108">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Alyssa Dineen
      </span>

    </button>

<div id="ember13167" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember13109" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember13110" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Alyssa Dineen"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember13111" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember13112" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-13113="13113">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Alyssa Dineen from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember13114" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember13116" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/anthonysaraceni/" id="ember13117" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember13118" class="presence-entity presence-entity--size-5 ember-view"><img alt="Anthony Saraceni" id="ember13119" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5603AQFtAZJVX7jw4g/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=9HLrOtyQ6jtRwHqWyBamYcS8MQQBxomwibhI0mCq4IE">

<div id="ember13120" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/anthonysaraceni/" id="ember13121" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Anthony Saraceni
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Senior Art Director at Fabletics
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember13122" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Anthony Saraceni" data-ember-action="" data-ember-action-13123="13123">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Anthony Saraceni
      </span>

    </button>

<div id="ember13169" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember13124" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember13125" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Anthony Saraceni"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember13126" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember13127" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-13128="13128">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Anthony Saraceni from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember13129" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember13172" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/ashley-helvey-81501a37/" id="ember13173" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember13174" class="presence-entity presence-entity--size-5 ember-view"><img alt="Ashley Helvey" id="ember13175" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4E03AQG4l7rWl0NDdg/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=2muzN4jbA2jgxZimCmtZaVvc4gOuimeLqYsI9oO9qT8">

<div id="ember13176" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/ashley-helvey-81501a37/" id="ember13177" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Ashley Helvey
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Creative Director represented by theCollectiveShift
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember13178" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Ashley Helvey" data-ember-action="" data-ember-action-13179="13179">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Ashley Helvey
      </span>

    </button>

<div id="ember13777" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember13180" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember13181" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Ashley Helvey"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember13182" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember13183" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-13184="13184">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Ashley Helvey from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember13185" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember13187" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/rhythmrevolution/" id="ember13188" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember13189" class="presence-entity presence-entity--size-5 ember-view"><img alt="Christopher Jonathan Brown" id="ember13190" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4E03AQGa8dtlMDpMkg/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=lzIXbN_MhoewKylkszbgQFQ7alTjEGg8XCyMjAH-ysI">

<div id="ember13191" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/rhythmrevolution/" id="ember13192" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Christopher Jonathan Brown
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Creative Director

    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember13193" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Christopher Jonathan Brown" data-ember-action="" data-ember-action-13194="13194">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Christopher Jonathan Brown
      </span>

    </button>

<div id="ember13771" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember13195" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember13196" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Christopher Jonathan Brown"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember13197" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember13198" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-13199="13199">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Christopher Jonathan Brown from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember13200" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember13202" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/harrison-budd-aaa00912/" id="ember13203" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember13204" class="presence-entity presence-entity--size-5 ember-view"><img alt="Harrison Budd" id="ember13205" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C5603AQFv635NCsaNfA/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=AAYpw3WPDwlGuViZ6FeA5PGcNuzk7s3l7L2xADeBFbc">

<div id="ember13206" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/harrison-budd-aaa00912/" id="ember13207" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Harrison Budd
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Digital Manager at Smashbox Studios
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember13208" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Harrison Budd" data-ember-action="" data-ember-action-13209="13209">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Harrison Budd
      </span>

    </button>

<div id="ember13772" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember13210" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember13211" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Harrison Budd"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember13212" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember13213" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-13214="13214">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Harrison Budd from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember13215" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember13217" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/carrie-barber-81210616/" id="ember13218" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember13219" class="presence-entity presence-entity--size-5 ember-view"><img alt="Carrie Barber" id="ember13220" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4D03AQHJ8DH0aZBZ6g/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=ize8xNLmMJ-b_P2nqPDe-jMyP8uHXYawD7v8Tb4btpA">

<div id="ember13221" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/carrie-barber-81210616/" id="ember13222" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Carrie Barber
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Freelance Senior Art Director at VIOLET GREY
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember13223" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Carrie Barber" data-ember-action="" data-ember-action-13224="13224">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Carrie Barber
      </span>

    </button>

<div id="ember13779" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember13225" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember13226" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Carrie Barber"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember13227" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember13228" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-13229="13229">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Carrie Barber from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember13230" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember13232" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/glenn-schuster-2005162a/" id="ember13233" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember13234" class="presence-entity presence-entity--size-5 ember-view"><img alt="Glenn Schuster" id="ember13235" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4D03AQFaT1TvKLp_Fg/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=J2m3N3dEnfqkLQFU38QM2rxPd-DsLzu3EPturGukKiw">

<div id="ember13236" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/glenn-schuster-2005162a/" id="ember13237" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Glenn Schuster
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Owner of Zen Space photo &amp; video studio
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember13238" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Glenn Schuster" data-ember-action="" data-ember-action-13239="13239">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Glenn Schuster
      </span>

    </button>

<div id="ember13773" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember13240" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember13241" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Glenn Schuster"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember13242" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember13243" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-13244="13244">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Glenn Schuster from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember13245" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember13247" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/alena-stefaniskova-923293118/" id="ember13248" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember13249" class="presence-entity presence-entity--size-5 ember-view"><img alt="Alena Stefaniskova" id="ember13250" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4D03AQH53ycw0HFqxg/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=FWsGuKPhslGFa6zaT-Ct0u9LKJ6XR5FRDYuUN6KfMUo">

<div id="ember13251" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/alena-stefaniskova-923293118/" id="ember13252" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Alena Stefaniskova
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Photographer / Retoucher / Digitech 
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember13253" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Alena Stefaniskova" data-ember-action="" data-ember-action-13254="13254">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Alena Stefaniskova
      </span>

    </button>

<div id="ember13778" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember13255" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember13256" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Alena Stefaniskova"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember13257" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember13258" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-13259="13259">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Alena Stefaniskova from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember13260" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember13262" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/bonnie-holland-photo/" id="ember13263" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember13264" class="presence-entity presence-entity--size-5 ember-view"><img alt="Bonnie Holland" id="ember13265" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4D03AQHLeeackfNi1Q/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=lKGCJqLb136nQLgwHiGxYmpzSvnhHWMHEBsQobdas68">

<div id="ember13266" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/bonnie-holland-photo/" id="ember13267" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Bonnie Holland
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Owner, Bonnie Holland Studio
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember13268" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Bonnie Holland" data-ember-action="" data-ember-action-13269="13269">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Bonnie Holland
      </span>

    </button>

<div id="ember13780" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember13270" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember13271" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Bonnie Holland"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember13272" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember13273" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-13274="13274">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Bonnie Holland from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember13275" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember13277" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/kyle-la-mere-29864b82/" id="ember13278" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember13279" class="presence-entity presence-entity--size-5 ember-view"><img alt="Kyle La Mere" id="ember13280" class=" presence-entity__image EntityPhoto-circle-5 lazy-image loaded ember-view" src="https://media.licdn.com/dms/image/C4E03AQEqSDZ9R6C7yQ/profile-displayphoto-shrink_100_100/0?e=1576713600&amp;v=beta&amp;t=3QbpFoVcMHDqlr1OYMXwK9jRIV2izsvp7YczVGiYZE8">

<div id="ember13281" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/kyle-la-mere-29864b82/" id="ember13282" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Kyle La Mere
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Designer / Photographer
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember13283" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Kyle La Mere" data-ember-action="" data-ember-action-13284="13284">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Kyle La Mere
      </span>

    </button>

<div id="ember13784" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember13285" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember13286" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Kyle La Mere"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember13287" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember13288" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-13289="13289">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Kyle La Mere from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember13290" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember13292" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/muriha-qidwai-263338160/" id="ember13293" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember13294" class="presence-entity presence-entity--size-5 ember-view"><img alt="Muriha Qidwai" id="ember13295" class=" presence-entity__image EntityPhoto-circle-5 lazy-image ember-view">

<div id="ember13296" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/muriha-qidwai-263338160/" id="ember13297" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Muriha Qidwai
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Enterprise Account Executive at globaledit®
    </span>
</a>    <time class="time-badge time-ago">
      Connected 1 week ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember13298" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Muriha Qidwai" data-ember-action="" data-ember-action-13299="13299">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Muriha Qidwai
      </span>

    </button>

<div id="ember13781" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember13300" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember13301" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Muriha Qidwai"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember13302" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember13303" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-13304="13304">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Muriha Qidwai from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember13305" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember13307" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/artdirectorswanted/" id="ember13308" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember13309" class="presence-entity presence-entity--size-5 ember-view"><img alt="Lukas Pludowski" id="ember13310" class=" presence-entity__image EntityPhoto-circle-5 lazy-image ember-view">

<div id="ember13311" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/artdirectorswanted/" id="ember13312" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Lukas Pludowski
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Freelance Creative Services
    </span>
</a>    <time class="time-badge time-ago">
      Connected 2 weeks ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember13313" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Lukas Pludowski" data-ember-action="" data-ember-action-13314="13314">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Lukas Pludowski
      </span>

    </button>

<div id="ember13774" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember13315" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember13316" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Lukas Pludowski"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember13317" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember13318" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-13319="13319">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Lukas Pludowski from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember13320" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember13322" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/janisceresi/" id="ember13323" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember13324" class="presence-entity presence-entity--size-5 ember-view"><img alt="Janis Ceresi" id="ember13325" class=" presence-entity__image EntityPhoto-circle-5 lazy-image ember-view">

<div id="ember13326" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/janisceresi/" id="ember13327" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Janis Ceresi
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Senior Creative Resource Manager
    </span>
</a>    <time class="time-badge time-ago">
      Connected 2 weeks ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember13328" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Janis Ceresi" data-ember-action="" data-ember-action-13329="13329">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Janis Ceresi
      </span>

    </button>

<div id="ember13775" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember13330" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember13331" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Janis Ceresi"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember13332" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember13333" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-13334="13334">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Janis Ceresi from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember13335" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember13337" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/cmdehague/" id="ember13338" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember13339" class="presence-entity presence-entity--size-5 ember-view"><img alt="Carmen DeHague (Lloyd)" id="ember13340" class=" presence-entity__image EntityPhoto-circle-5 lazy-image ember-view">

<div id="ember13341" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/cmdehague/" id="ember13342" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Carmen DeHague (Lloyd)
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Senior Interactive Designer - Target Creative
    </span>
</a>    <time class="time-badge time-ago">
      Connected 2 weeks ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember13343" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Carmen DeHague (Lloyd)" data-ember-action="" data-ember-action-13344="13344">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Carmen DeHague (Lloyd)
      </span>

    </button>

<div id="ember13782" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember13345" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember13346" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Carmen DeHague (Lloyd)"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember13347" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember13348" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-13349="13349">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Carmen DeHague (Lloyd) from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember13350" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember13352" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/paolo-ricartti-85691668/" id="ember13353" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember13354" class="presence-entity presence-entity--size-5 ember-view"><img alt="paolo ricartti" id="ember13355" class=" presence-entity__image EntityPhoto-circle-5 lazy-image ember-view">

<div id="ember13356" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/paolo-ricartti-85691668/" id="ember13357" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      paolo ricartti
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Producer | Photography | Video
    </span>
</a>    <time class="time-badge time-ago">
      Connected 2 weeks ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember13358" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to paolo ricartti" data-ember-action="" data-ember-action-13359="13359">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to paolo ricartti
      </span>

    </button>

<div id="ember13783" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember13360" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember13361" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for paolo ricartti"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember13362" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember13363" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-13364="13364">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove paolo ricartti from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember13365" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember13367" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/camilla-neilson-6667a260/" id="ember13368" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember13369" class="presence-entity presence-entity--size-5 ember-view"><img alt="Camilla Neilson" id="ember13370" class=" presence-entity__image EntityPhoto-circle-5 lazy-image ember-view">

<div id="ember13371" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/camilla-neilson-6667a260/" id="ember13372" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Camilla Neilson
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Studio Manager at URBN (Urban Outfitters, Anthropologie Group, Free People &amp; Nuuly)
    </span>
</a>    <time class="time-badge time-ago">
      Connected 2 weeks ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember13373" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Camilla Neilson" data-ember-action="" data-ember-action-13374="13374">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Camilla Neilson
      </span>

    </button>

<div id="ember13785" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember13375" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember13376" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Camilla Neilson"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember13377" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember13378" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-13379="13379">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Camilla Neilson from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember13380" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember13382" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/emmabett/" id="ember13383" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember13384" class="presence-entity presence-entity--size-5 ember-view"><img alt="Emma Bett" id="ember13385" class=" presence-entity__image EntityPhoto-circle-5 lazy-image ember-view">

<div id="ember13386" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/emmabett/" id="ember13387" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Emma Bett
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Creative Producer | Pentland Creative Agency
    </span>
</a>    <time class="time-badge time-ago">
      Connected 2 weeks ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember13388" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Emma Bett" data-ember-action="" data-ember-action-13389="13389">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Emma Bett
      </span>

    </button>

<div id="ember13786" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember13390" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember13391" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Emma Bett"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember13392" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember13393" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-13394="13394">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Emma Bett from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember13395" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember13397" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/lozanoricardo/" id="ember13398" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember13399" class="presence-entity presence-entity--size-5 ember-view"><img alt="Ricardo Lozano" id="ember13400" class=" presence-entity__image EntityPhoto-circle-5 lazy-image ember-view">

<div id="ember13401" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/lozanoricardo/" id="ember13402" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Ricardo Lozano
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Freelance Photographer at Nike
    </span>
</a>    <time class="time-badge time-ago">
      Connected 2 weeks ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember13403" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Ricardo Lozano" data-ember-action="" data-ember-action-13404="13404">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Ricardo Lozano
      </span>

    </button>

<div id="ember13788" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember13405" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember13406" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Ricardo Lozano"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember13407" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember13408" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-13409="13409">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Ricardo Lozano from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember13410" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember13412" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/csmcnally/" id="ember13413" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember13414" class="presence-entity presence-entity--size-5 ember-view"><img alt="Christopher McNally" id="ember13415" class=" presence-entity__image EntityPhoto-circle-5 lazy-image ember-view">

<div id="ember13416" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/csmcnally/" id="ember13417" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Christopher McNally
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Art Director
    </span>
</a>    <time class="time-badge time-ago">
      Connected 2 weeks ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember13418" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Christopher McNally" data-ember-action="" data-ember-action-13419="13419">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Christopher McNally
      </span>

    </button>

<div id="ember13787" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember13420" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember13421" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Christopher McNally"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember13422" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember13423" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-13424="13424">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Christopher McNally from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember13425" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember13427" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/ariel-lilly-26519910/" id="ember13428" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember13429" class="presence-entity presence-entity--size-5 ember-view"><img alt="Ariel Lilly" id="ember13430" class=" presence-entity__image EntityPhoto-circle-5 lazy-image ember-view">

<div id="ember13431" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/ariel-lilly-26519910/" id="ember13432" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Ariel Lilly
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Senior Account Manager at globaledit®
    </span>
</a>    <time class="time-badge time-ago">
      Connected 2 weeks ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember13433" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Ariel Lilly" data-ember-action="" data-ember-action-13434="13434">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Ariel Lilly
      </span>

    </button>

<div id="ember13789" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember13435" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember13436" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Ariel Lilly"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember13437" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember13438" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-13439="13439">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Ariel Lilly from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember13440" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember13442" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/paige-domine-222b2362/" id="ember13443" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember13444" class="presence-entity presence-entity--size-5 ember-view"><img alt="Paige Domine" id="ember13445" class=" presence-entity__image EntityPhoto-circle-5 lazy-image ember-view">

<div id="ember13446" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/paige-domine-222b2362/" id="ember13447" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Paige Domine
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Photo Agent at Walter Schupfer Management
    </span>
</a>    <time class="time-badge time-ago">
      Connected 2 weeks ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember13448" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Paige Domine" data-ember-action="" data-ember-action-13449="13449">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Paige Domine
      </span>

    </button>

<div id="ember13790" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember13450" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember13451" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Paige Domine"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember13452" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember13453" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-13454="13454">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Paige Domine from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember13455" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember13457" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/amydemidow/" id="ember13458" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember13459" class="presence-entity presence-entity--size-5 ember-view"><img alt="Amy Demidow" id="ember13460" class=" presence-entity__image EntityPhoto-circle-5 lazy-image ember-view">

<div id="ember13461" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/amydemidow/" id="ember13462" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Amy Demidow
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Fashion Photographer
    </span>
</a>    <time class="time-badge time-ago">
      Connected 2 weeks ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember13463" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Amy Demidow" data-ember-action="" data-ember-action-13464="13464">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Amy Demidow
      </span>

    </button>

<div id="ember13791" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember13465" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember13466" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Amy Demidow"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember13467" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember13468" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-13469="13469">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Amy Demidow from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember13470" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember13472" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/lauranovack/" id="ember13473" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember13474" class="presence-entity presence-entity--size-5 ember-view"><img alt="Laura Novack" id="ember13475" class=" presence-entity__image EntityPhoto-circle-5 lazy-image ember-view">

<div id="ember13476" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/lauranovack/" id="ember13477" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Laura Novack
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Associate Creative Director Copywriter &amp; Narrative/Script Writer | NY/LA/SF/CHI
    </span>
</a>    <time class="time-badge time-ago">
      Connected 2 weeks ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember13478" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Laura Novack" data-ember-action="" data-ember-action-13479="13479">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Laura Novack
      </span>

    </button>

<div id="ember13793" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember13480" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember13481" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Laura Novack"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember13482" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember13483" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-13484="13484">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Laura Novack from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember13485" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember13487" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/robert-bob-chapman-1b228b96/" id="ember13488" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember13489" class="presence-entity presence-entity--size-5 ember-view"><img alt="Robert.    Bob Chapman" id="ember13490" class=" presence-entity__image EntityPhoto-circle-5 lazy-image ember-view">

<div id="ember13491" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/robert-bob-chapman-1b228b96/" id="ember13492" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Robert.    Bob Chapman
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      --
    </span>
</a>    <time class="time-badge time-ago">
      Connected 2 weeks ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember13493" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Robert.    Bob Chapman" data-ember-action="" data-ember-action-13494="13494">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Robert.    Bob Chapman
      </span>

    </button>

<div id="ember13792" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember13495" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember13496" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Robert.    Bob Chapman"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember13497" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember13498" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-13499="13499">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Robert.    Bob Chapman from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember13500" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember13502" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/sandy-niellez-72516843/" id="ember13503" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember13504" class="presence-entity presence-entity--size-5 ember-view"><img alt="Sandy Niellez" id="ember13505" class=" presence-entity__image EntityPhoto-circle-5 lazy-image ember-view">

<div id="ember13506" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/sandy-niellez-72516843/" id="ember13507" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Sandy Niellez
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Nike Paris Creative Director
    </span>
</a>    <time class="time-badge time-ago">
      Connected 2 weeks ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember13508" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Sandy Niellez" data-ember-action="" data-ember-action-13509="13509">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Sandy Niellez
      </span>

    </button>

<div id="ember13794" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember13510" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember13511" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Sandy Niellez"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember13512" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember13513" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-13514="13514">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Sandy Niellez from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember13515" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember13517" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/tanya-silver-09b0262/" id="ember13518" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember13519" class="presence-entity presence-entity--size-5 ember-view"><img alt="Tanya Silver" id="ember13520" class=" presence-entity__image EntityPhoto-circle-5 lazy-image ember-view">

<div id="ember13521" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/tanya-silver-09b0262/" id="ember13522" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Tanya Silver
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Freelance Commercial + Film + Photography Producer
    </span>
</a>    <time class="time-badge time-ago">
      Connected 2 weeks ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember13523" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Tanya Silver" data-ember-action="" data-ember-action-13524="13524">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Tanya Silver
      </span>

    </button>

<div id="ember13795" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember13525" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember13526" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Tanya Silver"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember13527" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember13528" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-13529="13529">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Tanya Silver from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember13530" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember13532" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/michael-nahmias-3297bb14a/" id="ember13533" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember13534" class="presence-entity presence-entity--size-5 ember-view"><img alt="Michael Nahmias" id="ember13535" class=" presence-entity__image EntityPhoto-circle-5 lazy-image ember-view">

<div id="ember13536" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/michael-nahmias-3297bb14a/" id="ember13537" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Michael Nahmias
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Co-founder at fator.io
    </span>
</a>    <time class="time-badge time-ago">
      Connected 2 weeks ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember13538" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Michael Nahmias" data-ember-action="" data-ember-action-13539="13539">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Michael Nahmias
      </span>

    </button>

<div id="ember13796" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember13540" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember13541" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Michael Nahmias"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember13542" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember13543" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-13544="13544">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Michael Nahmias from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember13545" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember13547" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/david-newbury-092b8a4b/" id="ember13548" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember13549" class="presence-entity presence-entity--size-5 ember-view"><img alt="David Newbury" id="ember13550" class=" presence-entity__image EntityPhoto-circle-5 lazy-image ember-view">

<div id="ember13551" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/david-newbury-092b8a4b/" id="ember13552" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      David Newbury
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Partnerships Director at STUDIO BLUP - Creative Agency, London
    </span>
</a>    <time class="time-badge time-ago">
      Connected 2 weeks ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember13553" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to David Newbury" data-ember-action="" data-ember-action-13554="13554">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to David Newbury
      </span>

    </button>

<div id="ember13797" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember13555" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember13556" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for David Newbury"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember13557" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember13558" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-13559="13559">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove David Newbury from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember13560" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember13562" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/rebeccapatriciabaker/" id="ember13563" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember13564" class="presence-entity presence-entity--size-5 ember-view"><img alt="Rebecca Patricia Baker" id="ember13565" class=" presence-entity__image EntityPhoto-circle-5 lazy-image ember-view">

<div id="ember13566" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/rebeccapatriciabaker/" id="ember13567" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Rebecca Patricia Baker
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Senior Visual Merchandiser Womenswear Designer Studios at Selfridges
    </span>
</a>    <time class="time-badge time-ago">
      Connected 2 weeks ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember13568" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Rebecca Patricia Baker" data-ember-action="" data-ember-action-13569="13569">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Rebecca Patricia Baker
      </span>

    </button>

<div id="ember13798" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember13570" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember13571" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Rebecca Patricia Baker"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember13572" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember13573" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-13574="13574">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Rebecca Patricia Baker from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember13575" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember13577" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/christy-brown-7501473b/" id="ember13578" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember13579" class="presence-entity presence-entity--size-5 ember-view"><img alt="Christy Brown" id="ember13580" class=" presence-entity__image EntityPhoto-circle-5 lazy-image ember-view">

<div id="ember13581" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/christy-brown-7501473b/" id="ember13582" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Christy Brown
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Sr. Art Director/Design Director looking for opportunities
    </span>
</a>    <time class="time-badge time-ago">
      Connected 2 weeks ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember13583" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Christy Brown" data-ember-action="" data-ember-action-13584="13584">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Christy Brown
      </span>

    </button>

<div id="ember13799" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember13585" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember13586" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Christy Brown"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember13587" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember13588" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-13589="13589">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Christy Brown from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember13590" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember13592" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/ejieustaquio/" id="ember13593" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember13594" class="presence-entity presence-entity--size-5 ember-view"><img alt="Eji Eustaquio" id="ember13595" class=" presence-entity__image EntityPhoto-circle-5 lazy-image ember-view">

<div id="ember13596" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/ejieustaquio/" id="ember13597" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Eji Eustaquio
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Freelance Digital Technician
    </span>
</a>    <time class="time-badge time-ago">
      Connected 2 weeks ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember13598" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Eji Eustaquio" data-ember-action="" data-ember-action-13599="13599">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Eji Eustaquio
      </span>

    </button>

<div id="ember13800" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember13600" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember13601" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Eji Eustaquio"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember13602" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember13603" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-13604="13604">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Eji Eustaquio from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember13605" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember13607" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/brittney-knight/" id="ember13608" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember13609" class="presence-entity presence-entity--size-5 ember-view"><img alt="Brittney Knight" id="ember13610" class=" presence-entity__image EntityPhoto-circle-5 lazy-image ember-view">

<div id="ember13611" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/brittney-knight/" id="ember13612" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Brittney Knight
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Brand Designer II
    </span>
</a>    <time class="time-badge time-ago">
      Connected 2 weeks ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember13613" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Brittney Knight" data-ember-action="" data-ember-action-13614="13614">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Brittney Knight
      </span>

    </button>

<div id="ember13801" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember13615" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember13616" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Brittney Knight"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember13617" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember13618" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-13619="13619">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Brittney Knight from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember13620" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember13622" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/rosetedingcreative/" id="ember13623" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember13624" class="presence-entity presence-entity--size-5 ember-view"><img alt="Rose Teding" id="ember13625" class=" presence-entity__image EntityPhoto-circle-5 lazy-image ember-view">

<div id="ember13626" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/rosetedingcreative/" id="ember13627" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Rose Teding
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Creative Director | Art Director | Graphic Designer | Photographer
    </span>
</a>    <time class="time-badge time-ago">
      Connected 2 weeks ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember13628" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Rose Teding" data-ember-action="" data-ember-action-13629="13629">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Rose Teding
      </span>

    </button>

<div id="ember13776" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember13630" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember13631" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Rose Teding"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember13632" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember13633" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-13634="13634">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Rose Teding from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember13635" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember13637" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/sidney-diaz-0a3a156/" id="ember13638" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember13639" class="presence-entity presence-entity--size-5 ember-view"><img alt="Sidney Diaz" id="ember13640" class=" presence-entity__image EntityPhoto-circle-5 lazy-image ember-view">

<div id="ember13641" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/sidney-diaz-0a3a156/" id="ember13642" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Sidney Diaz
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Art Director at F&amp;M Expressions
    </span>
</a>    <time class="time-badge time-ago">
      Connected 2 weeks ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember13643" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Sidney Diaz" data-ember-action="" data-ember-action-13644="13644">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Sidney Diaz
      </span>

    </button>

<div id="ember13802" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember13645" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember13646" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Sidney Diaz"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember13647" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember13648" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-13649="13649">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Sidney Diaz from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember13650" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember13652" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/gustavo-c-45099745/" id="ember13653" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember13654" class="presence-entity presence-entity--size-5 ember-view"><img alt="Gustavo Chams" id="ember13655" class=" presence-entity__image EntityPhoto-circle-5 lazy-image ember-view">

<div id="ember13656" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/gustavo-c-45099745/" id="ember13657" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Gustavo Chams
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Fashion Photographer and Graphic Designer at Dish &amp; DUER
    </span>
</a>    <time class="time-badge time-ago">
      Connected 2 weeks ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember13658" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Gustavo Chams" data-ember-action="" data-ember-action-13659="13659">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Gustavo Chams
      </span>

    </button>

<div id="ember13803" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember13660" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember13661" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Gustavo Chams"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember13662" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember13663" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-13664="13664">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Gustavo Chams from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember13665" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember13667" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/jenny-sanchez-93b69767/" id="ember13668" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember13669" class="presence-entity presence-entity--size-5 ember-view"><img alt="Jenny Sanchez" id="ember13670" class=" presence-entity__image EntityPhoto-circle-5 lazy-image ember-view">

<div id="ember13671" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/jenny-sanchez-93b69767/" id="ember13672" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Jenny Sanchez
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Art Director at The Sandbox Agency
    </span>
</a>    <time class="time-badge time-ago">
      Connected 2 weeks ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember13673" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Jenny Sanchez" data-ember-action="" data-ember-action-13674="13674">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Jenny Sanchez
      </span>

    </button>

<div id="ember13805" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember13675" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember13676" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Jenny Sanchez"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember13677" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember13678" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-13679="13679">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Jenny Sanchez from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember13680" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember13682" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/melisamesa/" id="ember13683" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember13684" class="presence-entity presence-entity--size-5 ember-view"><img alt="Melisa Mesa" id="ember13685" class=" presence-entity__image EntityPhoto-circle-5 lazy-image ember-view">

<div id="ember13686" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/melisamesa/" id="ember13687" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Melisa Mesa
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Retoucher at YOOX NET-A-PORTER GROUP
    </span>
</a>    <time class="time-badge time-ago">
      Connected 2 weeks ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember13688" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Melisa Mesa" data-ember-action="" data-ember-action-13689="13689">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Melisa Mesa
      </span>

    </button>

<div id="ember13806" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember13690" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember13691" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Melisa Mesa"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember13692" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember13693" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-13694="13694">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Melisa Mesa from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember13695" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember13697" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/mike-keegan-0877a07a/" id="ember13698" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember13699" class="presence-entity presence-entity--size-5 ember-view"><img alt="Mike Keegan" id="ember13700" class=" presence-entity__image EntityPhoto-circle-5 lazy-image ember-view">

<div id="ember13701" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/mike-keegan-0877a07a/" id="ember13702" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Mike Keegan
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Jack-of-all-trades creative professional with over a decade worth of experience working with national and global brands.
    </span>
</a>    <time class="time-badge time-ago">
      Connected 2 weeks ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember13703" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Mike Keegan" data-ember-action="" data-ember-action-13704="13704">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Mike Keegan
      </span>

    </button>

<div id="ember13804" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember13705" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember13706" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Mike Keegan"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember13707" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember13708" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-13709="13709">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Mike Keegan from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember13710" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember13712" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/mauriciotorres987/" id="ember13713" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember13714" class="presence-entity presence-entity--size-5 ember-view"><img alt="Mauricio Torres" id="ember13715" class=" presence-entity__image EntityPhoto-circle-5 lazy-image ember-view">

<div id="ember13716" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/mauriciotorres987/" id="ember13717" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Mauricio Torres
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Art Director
    </span>
</a>    <time class="time-badge time-ago">
      Connected 2 weeks ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember13718" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Mauricio Torres" data-ember-action="" data-ember-action-13719="13719">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Mauricio Torres
      </span>

    </button>

<div id="ember13807" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember13720" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember13721" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Mauricio Torres"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember13722" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember13723" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-13724="13724">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Mauricio Torres from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember13725" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember13727" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/ashleysiech/" id="ember13728" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember13729" class="presence-entity presence-entity--size-5 ember-view"><img alt="Ashley Siech" id="ember13730" class=" presence-entity__image EntityPhoto-circle-5 lazy-image ember-view">

<div id="ember13731" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/ashleysiech/" id="ember13732" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Ashley Siech
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Brand and Media Manager  at HI-VIBE Superfood Juicery
    </span>
</a>    <time class="time-badge time-ago">
      Connected 2 weeks ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember13733" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Ashley Siech" data-ember-action="" data-ember-action-13734="13734">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Ashley Siech
      </span>

    </button>

<div id="ember13809" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember13735" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember13736" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Ashley Siech"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember13737" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember13738" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-13739="13739">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Ashley Siech from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember13740" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember13742" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/maya-valentine-215523156/" id="ember13743" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember13744" class="presence-entity presence-entity--size-5 ember-view"><img alt="Maya Valentine" id="ember13745" class=" presence-entity__image EntityPhoto-circle-5 lazy-image ember-view">

<div id="ember13746" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/maya-valentine-215523156/" id="ember13747" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Maya Valentine
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Photo Editor at Columbia Missourian
    </span>
</a>    <time class="time-badge time-ago">
      Connected 2 weeks ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember13748" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Maya Valentine" data-ember-action="" data-ember-action-13749="13749">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Maya Valentine
      </span>

    </button>

<div id="ember13808" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember13750" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember13751" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Maya Valentine"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember13752" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember13753" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-13754="13754">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Maya Valentine from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember13755" class="ember-view"><!----></div></div>
      </li>
      <li class="list-style-none">
        <div id="ember13757" class="mn-connection-card ember-view"><a data-control-name="connection_profile" href="/in/cody-welchlin-415a85143/" id="ember13758" class="mn-connection-card__picture pt2 pr2 pb1 pl5  ember-view">  <div id="ember13759" class="presence-entity presence-entity--size-5 ember-view"><img alt="Cody Welchlin" id="ember13760" class=" presence-entity__image EntityPhoto-circle-5 lazy-image ember-view">

<div id="ember13761" class=" presence-entity__indicator presence-entity__indicator--size-5 presence-indicator hidden presence-indicator--size-5 ember-view">
<span class="visually-hidden">
    Status is offline
  </span>
</div>
</div>
</a>
<div class="mn-connection-card__details">
<a data-control-name="connection_profile" href="/in/cody-welchlin-415a85143/" id="ember13762" class="mn-connection-card__link ember-view">    <span class="visually-hidden">Member’s name</span>
    <span class="mn-connection-card__name t-16 t-black t-bold">
      Cody Welchlin
    </span>
    <span class="visually-hidden">Member’s occupation</span>
    <span class="mn-connection-card__occupation t-14 t-black--light t-normal">
      Photo Stylist
    </span>
</a>    <time class="time-badge time-ago">
      Connected 2 weeks ago
    </time>
  
</div>

<div class="mn-connection-card__action-container pl3 pr2">
<div data-control-name="message" id="ember13763" class="ember-view">    <button class="message-anywhere-button artdeco-button artdeco-button--secondary" aria-label="Send message to Cody Welchlin" data-ember-action="" data-ember-action-13764="13764">
              <span aria-hidden="true">Message</span>
      <span class="visually-hidden">
        Send a message to Cody Welchlin
      </span>

    </button>

<div id="ember13810" class="ember-view"><!----></div></div>

<artdeco-dropdown id="ember13765" class="mn-connection-card__dropdown ml1 ember-view"><artdeco-dropdown-trigger aria-expanded="false" data-control-name="ellipsis" role="button" placement="bottom" id="ember13766" class="mn-connection-card__dropdown-trigger ember-view" tabindex="0">      <li-icon type="ellipsis-horizontal-icon" size="medium" role="img" aria-label="More actions for Cody Welchlin"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M2,10H6v4H2V10Zm8,4h4V10H10v4Zm8-4v4h4V10H18Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>

<!----></artdeco-dropdown-trigger><artdeco-dropdown-content arrow-dir="right" justification="right" placement="bottom" data-dropdown="" tabindex="-1" aria-hidden="true" id="ember13767" class="artdeco-dropdown-with-arrow ember-view">  <!----><artdeco-dropdown-item data-dropdown="" id="ember13768" class="mn-connection-card__dropdown-item ember-view"><!---->        <button class="display-flex align-items-center t-14 t-black--light t-normal" aria-label="Remove  from connections" data-ember-action="" data-ember-action-13769="13769">
          <li-icon type="trash-icon" class="mn-connection-card__dropdown-option-icon" size="medium" role="img" aria-label="Remove Cody Welchlin from connections"><svg viewBox="0 0 24 24" width="24px" height="24px" x="0" y="0" preserveAspectRatio="xMinYMin meet" class="artdeco-icon" focusable="false"><path d="M19.26,2.9A28,28,0,0,0,15,2.13V1.5A0.5,0.5,0,0,0,14.5,1h-5a0.5,0.5,0,0,0-.5.5V2.13a28,28,0,0,0-4.26.78,1,1,0,0,0-.74,1V9H5V21a1,1,0,0,0,1,1H18a1,1,0,0,0,1-1V9h1V3.88A1,1,0,0,0,19.26,2.9ZM17,20H7V9H17V20ZM18,7H6V4.59a26.35,26.35,0,0,1,6-.71,26.35,26.35,0,0,1,6,.71V7ZM11,18H10V11h1v7Zm3,0H13V11h1v7Z" class="large-icon" style="fill: currentColor"></path></svg></li-icon>
          <span class="mn-connection-card__dropdown-option-text ml1">Remove connection</span>
        </button>
</artdeco-dropdown-item>
</artdeco-dropdown-content></artdeco-dropdown></div>

<div id="ember13770" class="ember-view"><!----></div></div>
      </li>
  </ul> '''
soup = BeautifulSoup(html_source, 'html.parser')
new_contacts = soup.find_all('div', class_='mn-connection-card__details')
for profile in new_contacts:
        profile_link = profile.find_all('a')[0]['href']
        profile_link = "https://www.linkedin.com" + profile_link
        profile_name = profile.find('span', class_='mn-connection-card__name t-16 t-black t-bold').text
        profile_title = profile.find('span', class_='mn-connection-card__occupation t-14 t-black--light t-normal').text
        profile_time = profile.find('time', class_='time-badge time-ago').text
        row = profile_link + ' # ' + profile_name.replace("\n", "") + "#" + profile_title.replace("\n", "") + ' # ' + profile_time.replace("\n", "")
        print(row)

