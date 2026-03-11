// aProject/ui/app/components/viewer.tsx

interface viewerProps{
  url: string | null;
}

export const Viewer = ({url}:viewerProps)=>{
  return(
    <>
    {
      url?(<img src={url}/>):(<p> no url found </p>)
    }
    </>
  )
}
