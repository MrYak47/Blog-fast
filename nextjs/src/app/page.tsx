"use client"

import { Post, IPost } from "@/components/post"
import "@/app/(root)/root.css"
import Link from "next/link"
import {useEffect, useState} from "react"



export default function Home() {
  const [postsD, setPostsD] = useState<IPost[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const fetchPosts = async () => {
      try {
        // Fetch all posts
        const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/posts/?limit=10`)
        if(!res.ok) throw new Error('Failed to fetch posts')

        setPostsD(await res.json()) 
        
      } catch (error) {
        console.error('Error fetching posts:', error)
      } finally {
        setLoading(false)
      }
    }
    
    fetchPosts()
    
  }, [])

  
  return (
    <>
      <h1 className="title">Home</h1>
      {loading ? (
        <div className="text-center py-8">Loading posts...</div>
      ) : (
        <>
          <ul className="posts">
          {postsD && postsD.length > 0 ? postsD.map((post: IPost) => (
            <li key={post.id}>
              <Link href={`/post/${post.slug}`} className="no-underline">
                <Post {...post} />
              </Link>
            </li>
          )) : (
            <li className="text-center py-8">No posts found</li>
          )}
          </ul>
        </>
      )}
    </>
  )
}
