import React from 'react';
import { Pressable, StyleSheet, Text, useWindowDimensions, View } from 'react-native';

export function AuroraNativeHero({ onPress }: { onPress?: () => void }) {
  const compact = useWindowDimensions().width < 600;
  return (
    <View style={[styles.hero, compact && styles.compact]}>
      <View style={styles.glowA} />
      <View style={styles.glowB} />
      <Text style={styles.title}>AI workspace</Text>
      <Text style={styles.body}>Aurora is atmosphere. Foreground content stays semantic and readable without the glow.</Text>
      <Pressable accessibilityRole="button" accessibilityState={{ disabled: !onPress }} disabled={!onPress} onPress={onPress} style={({ pressed }) => [styles.button, pressed && styles.pressed]}>
        <Text style={styles.label}>Explore</Text>
      </Pressable>
    </View>
  );
}

const styles = StyleSheet.create({
  hero: { minHeight: 220, overflow: 'hidden', padding: 20, borderRadius: 24, backgroundColor: '#17243b' },
  compact: { padding: 16 },
  glowA: { position: 'absolute', width: 180, height: 180, borderRadius: 90, backgroundColor: '#7068ff', opacity: 0.42, top: -70, left: -30 },
  glowB: { position: 'absolute', width: 150, height: 150, borderRadius: 75, backgroundColor: '#55d9c8', opacity: 0.35, bottom: -60, right: -20 },
  title: { fontSize: 22, fontWeight: '800', color: '#fff' },
  body: { marginTop: 8, color: '#e9edf7' },
  button: { marginTop: 18, minHeight: 48, paddingHorizontal: 18, justifyContent: 'center', borderRadius: 16, backgroundColor: '#ffffff' },
  pressed: { opacity: 0.8 },
  label: { textAlign: 'center', fontWeight: '700', color: '#182238' },
});

// Verification: atmospheric layer is decorative, foreground contrast and native state are independent.
// Fallback: remove both glow layers and retain the solid hero surface and interaction.
