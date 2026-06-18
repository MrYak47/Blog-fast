"use client"

import { Post, IPost } from "@/components/post"
import "@/app/(root)/root.css"
import Link from "next/link"
import { useEffect, useState } from "react"

interface IPostWithAuthor extends IPost {
   author_name?: string;
   author_image?: string;
}

export default function ExplorePage() {
   const [postsD, setPostsD] = useState<IPostWithAuthor[]>([])
   const [loading, setLoading] = useState(true)
   const [hasMore, setHasMore] = useState(true)
   const [skip, setSkip] = useState(0)
   const limit = 10

useEffect(() => {
   const fetchPosts = async () => {
         try {
            setLoading(true)
            // Fetch latest posts with pagination
            const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/posts?skip=${skip}&limit=${limit}`)
            if (!res.ok) throw new Error(`HTTP ${res.status}`);
            const data = await res.json()
            const flat = data.map((post: any) => ({
               ...post,
               author_name: post.author.username,
               author_image: post.author.image_url || "/default.jpg"
            }))
            
            setPostsD(flat)
            setHasMore(data.length === limit)

         } catch (error) {
            console.error('Error fetching posts:', error)
         } finally {
            setLoading(false)
         }
      }
      fetchPosts()
   }, [skip])

   const handleNext = () => setSkip(skip + limit)
   const handlePrev = () => setSkip(Math.max(0, skip - limit))

   return (
      <>
      <h1 className="title">Explore Latest Posts</h1>
      
      {loading ? (
         <div className="text-center py-8">Loading posts...</div>
      ) : (
         <>
            <ul className="posts">
            {postsD && postsD.length > 0 ? postsD.map((post: IPostWithAuthor) => (
               <li key={post.id}>
                  <Link href={`/post/${post.slug}`} className="no-underline">
                  <Post {...post} />
                  </Link>
               </li>
            )) : (
               <li className="text-center py-8">No posts found</li>
            )}
            </ul>
            
            {/* Pagination Controls */}
            <div className="flex justify-center gap-4 mt-8 pb-8">
            <button
               onClick={handlePrev}
               disabled={skip === 0}
               className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 disabled:bg-gray-400 disabled:cursor-not-allowed"
            >
               ← Previous
            </button>
            <span className="py-2 text-gray-600">
               Page {Math.floor(skip / limit) + 1}
            </span>
            <button
               onClick={handleNext}
               disabled={!hasMore}
               className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 disabled:bg-gray-400 disabled:cursor-not-allowed"
            >
               Next →
            </button>
            </div>
         </>
      )}
      </>
   )
}
