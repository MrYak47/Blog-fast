import { Post, IPost } from "@/components/post"
import "@/app/(root)/root.css"
import {posts} from "@/components/posts"
import Link from "next/link"








export default function Home() {


  return (
    <>
      <h1 className="title">Home</h1>
      <>
        <ul className="posts">
        {posts && posts.length > 0 && posts.map((post: IPost) => (
          <li key={post.id as unknown as string}>
            <Link href={`/post/${post.slug}`} className="no-underline">
              <Post pro_pic={post.pro_pic} id={post.id} slug={post.slug} author={post.author} title={post.title} content={post.content} />
            </Link>
          </li>

        ))}
        </ul>
      </>
    </>



    
    
  )
}
