"""
Mock Application Endpoint for Testing Azure AI Evaluation

This mock endpoint simulates a RAG application that answers questions about 
Microsoft Responsible AI without requiring an actual deployed endpoint.

To use this:
1. In Manual_Evaluation.ipynb, change:
   from application_endpoint import ApplicationEndpoint
   to:
   from application_endpoint_mock import ApplicationEndpoint
"""

from typing_extensions import Self
from typing import TypedDict
import random


class ApplicationEndpoint:
    def __init__(self: Self) -> None:
        print("🔧 Using MOCK Application Endpoint (for testing only)")
        
        # Mock knowledge base about Microsoft Responsible AI
        self.knowledge_base = {
            "fairness": "Microsoft's Responsible AI Standard emphasizes that AI systems should treat all people fairly. This includes identifying and mitigating unfair bias in AI systems.",
            "reliability": "AI systems should perform reliably and safely under normal circumstances and in unexpected conditions. Systems should be rigorously tested before deployment.",
            "safety": "AI systems should be safe and not cause harm to people or society. Safety measures should be built into the design and operation of AI systems.",
            "privacy": "AI systems should respect privacy and protect personal data. Data collection should be transparent and users should have control over their data.",
            "inclusiveness": "AI systems should be designed to be inclusive and accessible to all people, regardless of ability, age, gender, race, or other factors.",
            "transparency": "AI systems should be understandable. People should know when they're interacting with AI and understand how decisions are made.",
            "accountability": "People who design and deploy AI systems should be accountable for how their systems operate. Clear governance structures should be in place.",
        }

    class Response(TypedDict):
        query: str
        response: str

    def __call__(self: Self, query: str, context: str = "") -> Response:
        """
        Simulates calling a RAG application endpoint.
        
        Args:
            query: The user's question
            context: Additional context (optional)
            
        Returns:
            Dictionary with query and response
        """
        
        # Simple keyword-based response generation
        query_lower = query.lower()
        
        # Try to match keywords to knowledge base
        response_text = None
        for topic, answer in self.knowledge_base.items():
            if topic in query_lower:
                response_text = answer
                break
        
        # Default response if no match found
        if not response_text:
            response_text = (
                "Microsoft's Responsible AI Standard provides a framework for developing "
                "AI systems responsibly. It covers principles including fairness, reliability, "
                "safety, privacy, inclusiveness, transparency, and accountability. Each principle "
                "provides guidance for building trustworthy AI systems."
            )
        
        # Simulate slight variation in responses (like a real LLM would have)
        variations = [
            response_text,
            f"Based on Microsoft's Responsible AI guidelines: {response_text}",
            f"According to the Responsible AI Standard: {response_text}",
        ]
        
        final_response = random.choice(variations)
        
        print(f"📝 Mock query: {query[:50]}...")
        print(f"📝 Mock response: {final_response[:100]}...")
        
        return {
            "query": query,
            "response": final_response
        }
