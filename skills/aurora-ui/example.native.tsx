import React from 'react';
import { Pressable, StyleSheet, Text, useWindowDimensions, View } from 'react-native';

export function AuroraNativeHero({ onPress, effectsEnabled = true }: { onPress?: () => void; effectsEnabled?: boolean }) {
  const compact = useWindowDimensions().width < 600;
  return (
    <View style={[styles.hero, compact && styles.compact]}>
      {effectsEnabled && (
        <View pointerEvents="none" accessible={false} importantForAccessibility="no-hide-descendants" style={StyleSheet.absoluteFill}>
          <View style={styles.glowA} />
          <View style={styles.glowB} />
        </View>
      )}
      <Text accessibilityRole="header" style={styles.title}>Create something remarkable</Text>
      <Text style={styles.body}>The Aurora layer adds atmosphere while the content remains stable and readable.</Text>
      <Pressable
        accessibilityRole="button"
        accessibilityState={{ disabled: !onPress }}
        disabled={!onPress}
        onPress={onPress}
        style={({ pressed }) => [styles.button, pressed && styles.pressed]}
      >
        <Text style={styles.label}>Explore</Text>
      </Pressable>
    </View>
  );
}

const styles = StyleSheet.create({
  hero: { minHeight: 220, overflow: 'hidden', padding: 20, borderRadius: 24, backgroundColor: '#0d1021' },
  compact: { padding: 16 },
  glowA: { position: 'absolute', width: 180, height: 180, borderRadius: 90, backgroundColor: '#6d5dfc', opacity: 0.42, top: -70, left: -30 },
  glowB: { position: 'absolute', width: 150, height: 150, borderRadius: 75, backgroundColor: '#19c6b5', opacity: 0.35, bottom: -60, right: -20 },
  title: { fontSize: 22, fontWeight: '800', color: '#fff' },
  body: { marginTop: 8, color: '#e9edf7' },
  button: { marginTop: 18, minHeight: 48, paddingHorizontal: 18, justifyContent: 'center', borderRadius: 16, backgroundColor: '#ffffff' },
  pressed: { opacity: 0.8 },
  label: { textAlign: 'center', fontWeight: '700', color: '#182238' },
});

// Fallback: set effectsEnabled=false; content, state, target size, and interaction remain unchanged.
