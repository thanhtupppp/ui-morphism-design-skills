import React from 'react';
import { Pressable, StyleSheet, Text, useWindowDimensions, View } from 'react-native';

export function NeumorphismNativeCard({ onPress }: { onPress?: () => void }) {
  const compact = useWindowDimensions().width < 600;
  return (
    <View style={[styles.card, compact && styles.compact]}>
      <Text style={styles.title}>Soft control</Text>
      <Text style={styles.body}>Treat paired shadows as optional decoration, not as the state channel.</Text>
      <Pressable accessibilityRole="button" accessibilityState={{ disabled: !onPress }} disabled={!onPress} onPress={onPress} style={({ pressed }) => [styles.button, pressed && styles.pressed]}>
        <Text style={styles.label}>{onPress ? 'Press' : 'Unavailable'}</Text>
      </Pressable>
    </View>
  );
}

const styles = StyleSheet.create({
  card: { padding: 20, borderRadius: 24, backgroundColor: '#e7e9ee', shadowColor: '#6d7180', shadowOpacity: 0.24, shadowRadius: 10, shadowOffset: { width: 6, height: 6 }, elevation: 6 },
  compact: { padding: 16 },
  title: { fontSize: 20, fontWeight: '700' },
  body: { marginTop: 8, color: '#3e424b' },
  button: { marginTop: 16, minHeight: 48, paddingHorizontal: 18, justifyContent: 'center', borderRadius: 18, borderWidth: 1, borderColor: '#c1c4cb', backgroundColor: '#e7e9ee' },
  pressed: { shadowOpacity: 0.08, elevation: 1, transform: [{ translateY: 1 }] },
  label: { textAlign: 'center', fontWeight: '700' },
});

// Verification: native semantics, explicit pressed/disabled state, compact adaptation, decorative shadow isolation.
// Fallback: remove shadows and retain border, fill, text, and state.
