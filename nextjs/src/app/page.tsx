import Post from "@/components/post"








export default function Home() {
  

    
  const posts= [
    {
      "id" : "1",
      "author" : "Brody Larriton",
      "title": "Why I Love FastAPI",
      "content": "FastAPI has completely changed how I build APIs. The automatic documentation, type hints, and async support make development so much faster. Plus, the performance is incredible!",
    },
    {
      "id" : "2",
      "author": "Mack Johnson",
      "title": "Corey Schafer Has the Best YouTube Tutorials!",
      "content": "This was written by a viewer and definitely not by me... I mean him. Totally not written by him, but by me... a real viewer. Seriously, check out his channel for amazing Python content.",
    }
  ]





  return (
    <>
      <h1 className="title">Home</h1>
      <>
        <ul className="posts">
        {post && post.len

        }
        </ul>
      </>
    </>



    
    
  )
}
