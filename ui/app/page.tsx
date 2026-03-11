// aProject/ui/app/page.tsx
"use client";
import {useState, useEffect} from 'react';

import "./globals.css";
import {Viewer} from './components/viewer';
import {default_url, api_domain} from './config';
export default function Home(){
  const [prompt, setPrompt] = useState("");
  const [url, setUrl] = useState(default_url);
  const [isLoading, setIsLoading] = useState(false);
  async function fetchImage(){
    setIsLoading(true);
    const res = await  fetch(`${api_domain}/generate/${prompt}/1`);
    const data = await res.json();
    setUrl(data.data[0]);
    setIsLoading(false);
  }
  return (
    <>
    <header>Image Generator APP</header>
    <main>
      <section style = {{display: 'flex' ,flexDirection:'column'}}>
        <textarea className="prompt" value={prompt} placeholder="Enter something you want to generate" onChange={(e)=>setPrompt(e.target.value)}></textarea>
        <button className="submit" disabled={isLoading}  onClick={()=>fetchImage()}  >Submit</button>
      </section> 
      <section>
      {
        isLoading?(<span>....Image Loading</span>):
          (<Viewer url={url}/>)
      }
      </section>

    </main>
    <footer>Joelinator</footer>
    </>
      )
}
