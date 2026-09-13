import React from 'react';
import { Pressable, StyleSheet, Text, useWindowDimensions, View } from 'react-native';

export function MaterialDesignNativeCard({ onPress }: { onPress?: () => void }) {
  const compact = useWindowDimensions().width < 600;
  return (
    <View style={[styles.card, compact && styles.compact]}>
      <Text style={styles.title}>Material action</Text>
      <Text style={styles.body}>Keep component hierarchy and state layers native; elevation is secondary.</Text>
      <Pressable accessibilityRole="button" accessibilityState={{ disabled: !onPress }} disabled={!onPress} onPress={onPress} style={({ pressed }) => [styles.button, pressed && styles.pressed]}>
        <Text style={styles.label}>Continue</Text>
      </Pressable>
    </View>
  );
}

const styles = StyleSheet.create({
  card: { padding: 20, borderRadius: 14, backgroundColor: '#ffffff', shadowColor: '#000000', shadowOpacity: 0.18, shadowRadius: 8, shadowOffset: { width: 0, height: 3 }, elevation: 3 },
  compact: { padding: 16 },
  title: { fontSize: 20, fontWeight: '700' },
  body: { marginTop: 8, color: '#303030' },
  button: { marginTop: 16, minHeight: 48, paddingHorizontal: 18, justifyContent: 'center', borderRadius: 22, backgroundColor: '#e9eefc' },
  pressed: { opacity: 0.82 },
  label: { textAlign: 'center', fontWeight: '700' },
});

// Verification: Pressable semantics, pressed/disabled state, compact adaptation, bounded elevation.
// Fallback: use a flat surface and explicit border/state without changing hierarchy.
