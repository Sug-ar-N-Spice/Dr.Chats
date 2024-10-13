//import React from 'react'
import { View, Text, ScrollView, TouchableOpacity, StyleSheet } from 'react-native'
import { SafeAreaView } from 'react-native-safe-area-context'
import { MessageCircle, Calendar, User, CheckSquare, BookOpen, ChevronRight } from 'lucide-react-native'

export default function MainScreen() {
  const features = [
    { icon: MessageCircle, title: 'AI Chatbot', description: 'Get quick answers to your questions' },
    { icon: Calendar, title: 'Live Chat with Doctors', description: 'Schedule appointments or chat in real-time' },
    { icon: User, title: 'Anonymous Interaction', description: 'Your privacy is our priority' },
    { icon: CheckSquare, title: 'Symptom Checker', description: 'Input symptoms for preliminary advice' },
    { icon: BookOpen, title: 'Resource Library', description: 'Access information on STI prevention and treatment' },
  ]

  return (
    <SafeAreaView style={styles.container}>
      <ScrollView contentContainerStyle={styles.scrollContent}>
        <Text style={styles.title}>Dr.CHATS</Text>
        <Text style={styles.subtitle}>Your Confidential Health Assistant</Text>
        
        {features.map((feature, index) => (
          <TouchableOpacity key={index} style={styles.featureCard}>
            <View style={styles.iconContainer}>
              <feature.icon color="#4A5568" size={24} />
            </View>
            <View style={styles.featureContent}>
              <Text style={styles.featureTitle}>{feature.title}</Text>
              <Text style={styles.featureDescription}>{feature.description}</Text>
            </View>
            <ChevronRight color="#4A5568" size={24} />
          </TouchableOpacity>
        ))}
      </ScrollView>
    </SafeAreaView>
  )
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F7FAFC',
  },
  scrollContent: {
    padding: 20,
  },
  title: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#2D3748',
    marginBottom: 8,
  },
  subtitle: {
    fontSize: 18,
    color: '#4A5568',
    marginBottom: 24,
  },
  featureCard: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#FFFFFF',
    borderRadius: 12,
    padding: 16,
    marginBottom: 16,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 1 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 2,
  },
  iconContainer: {
    width: 48,
    height: 48,
    borderRadius: 24,
    backgroundColor: '#EBF8FF',
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: 16,
  },
  featureContent: {
    flex: 1,
  },
  featureTitle: {
    fontSize: 18,
    fontWeight: '600',
    color: '#2D3748',
    marginBottom: 4,
  },
  featureDescription: {
    fontSize: 14,
    color: '#4A5568',
  },
})
//  main.swift
//  Dr. CHATS
//
//  Created by Simon Ponce-Potes on 10/11/24.
//

import Foundation

print("Hello, World!")

